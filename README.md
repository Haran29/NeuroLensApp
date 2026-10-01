# NeuroLensApp

NeuroLensApp is a full-stack Parkinson’s risk-assessment platform:
- **Frontend:** Expo + React Native mobile app (`frontend/NeuroLens`)
- **Backend:** FastAPI service for multimodal analysis (`backend`)

The app collects wearable, voice, drawing, and cognitive signals and presents a combined risk assessment with history tracking.

## Repository Structure

```text
NeuroLensApp/
├── frontend/
│   └── NeuroLens/          # Expo/React Native app (TypeScript)
├── backend/                # FastAPI app + ML inference services (Python)
├── cloudbuild.yaml         # Cloud Build / Cloud Run deployment config
└── README.md
```

## Tech Stack

### Frontend
- Expo SDK 54
- React Native + TypeScript
- Expo Router
- Axios
- Firebase Auth

### Backend
- FastAPI + Uvicorn
- Firebase Admin SDK + Firestore
- Pydantic Settings
- NumPy / pandas / SciPy / scikit-learn / PyTorch
- Whisper + audio feature extraction tooling

## Prerequisites

- Node.js 18+ and npm
- Python 3.10+
- Firebase project credentials for backend auth/firestore
- Android Studio / Xcode (for native mobile targets)

## Quick Start

Run frontend and backend in separate terminals.

### 1) Backend setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: .\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Backend default URL: `http://localhost:8000`

### 2) Frontend setup

```bash
cd frontend/NeuroLens
npm install
npm start
```

Useful frontend scripts:

```bash
npm run android
npm run ios
npm run web
npm run lint
npm run build
```

## Environment Configuration

### Backend (`backend/.env`)

Use `backend/.env.example` as a template.

| Variable | Purpose | Default |
|---|---|---|
| `API_V1_STR` | API prefix | `/api` |
| `PROJECT_NAME` | OpenAPI/app title | `NeuroLens API` |
| `LOG_LEVEL` | Backend log level | `INFO` |
| `DATABASE_URL` | Local DB URL (legacy/local tooling) | `sqlite:///./neurolens.db` |
| `FIREBASE_ADMIN_SDK_PATH` | Firebase Admin JSON path (relative to `backend/` or absolute) | `firebase-admin-sdk.json` |
| `BACKEND_CORS_ORIGINS` | Allowed origins (comma-separated or JSON list) | `*` |
| `MODEL_SERVER_URL` | Optional remote model endpoint | HF Space URL |

### Frontend

| Variable | Purpose |
|---|---|
| `EXPO_PUBLIC_API_BASE_URL` | Override backend base URL for device/emulator testing |

If not set, the app uses the currently configured deployed backend URL in `frontend/NeuroLens/constants/api.ts`.

## Frontend/Backend Workflow

- Frontend API client: `frontend/NeuroLens/services/api.ts`
- Backend route registration: `backend/main.py`
- API modules: `backend/app/routes/*`
- Multimodal endpoints used by the app:
  - `GET /api/multimodal/history`
  - `GET /api/multimodal/latest`
  - `POST /api/multimodal/result/{session_id}`

## Validation Commands

### Frontend
```bash
cd frontend/NeuroLens
npm run lint
```

### Backend
```bash
cd backend
python -m compileall main.py app
```

> Note: There is currently no established backend test suite in `backend/tests`.

## Deployment

`cloudbuild.yaml` builds the backend Docker image and deploys it to Cloud Run.

## Troubleshooting

- **`expo: not found` when running lint/start**
  - Run `npm install` inside `frontend/NeuroLens`.

- **401/403 from backend auth endpoints**
  - Confirm Firebase Admin credentials exist at `FIREBASE_ADMIN_SDK_PATH`.
  - Ensure the frontend token is being stored and sent in `Authorization` headers.

- **Mobile app cannot hit local backend**
  - Set `EXPO_PUBLIC_API_BASE_URL` to a reachable host/IP and restart Expo.

- **Health diagnostics indicate missing model files**
  - Check `backend/app/models` artifacts and deployment packaging.

## Security Notes

- Never commit Firebase service-account files, tokens, or private credentials.
- Keep `.env` local and use secret managers in deployed environments.

## License

No explicit license is currently defined in this repository.
