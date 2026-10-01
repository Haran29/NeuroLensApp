import logging
from pathlib import Path

import firebase_admin
from fastapi import HTTPException, status
from firebase_admin import auth, credentials

from .config import settings

logger = logging.getLogger(__name__)


# Initialize Firebase Admin SDK
def initialize_firebase() -> bool:
    """Initialize Firebase Admin SDK if credentials are available."""
    try:
        firebase_admin.get_app()
        return True
    except ValueError:
        pass

    cred_path = Path(settings.FIREBASE_ADMIN_SDK_PATH)
    if not cred_path.is_absolute():
        backend_root = Path(__file__).resolve().parents[2]
        cred_path = backend_root / cred_path

    if not cred_path.exists():
        logger.warning(
            "Firebase credentials file not found at %s. Authentication endpoints will be unavailable.",
            cred_path,
        )
        return False

    cred = credentials.Certificate(str(cred_path))
    firebase_admin.initialize_app(cred)
    logger.info("Firebase Admin SDK initialized successfully")
    return True


async def verify_firebase_token(token: str) -> dict:
    """Verify Firebase ID token and return user info."""
    try:
        firebase_admin.get_app()
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Authentication service is not configured",
        )

    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except auth.InvalidIdTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
        )
    except auth.ExpiredIdTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication token has expired",
        )
    except Exception:
        logger.exception("Unexpected Firebase token verification failure")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed",
        )
