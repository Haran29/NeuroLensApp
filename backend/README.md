# NeuroLens Backend

FastAPI service powering authentication, assessment ingestion, and multimodal risk aggregation.

## Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: .\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

Default URL: `http://localhost:8000`

## Environment

Create `backend/.env` using `backend/.env.example`.

Important variables:
- `FIREBASE_ADMIN_SDK_PATH`
- `BACKEND_CORS_ORIGINS`
- `API_V1_STR`
- `PROJECT_NAME`
- `LOG_LEVEL`
- `MODEL_SERVER_URL`

## Validation

```bash
python -m compileall main.py app
```

## Health endpoints

- `GET /health/ready` – readiness probe
- `GET /health/diagnostics` – model/dependency diagnostics
