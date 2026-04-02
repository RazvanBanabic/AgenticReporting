# AgenticReporting

A project that implements AI agents for financial reporting and data visualization.

## Backend Setup

This repository now includes a production-oriented FastAPI backend scaffold with:

- FastAPI entry point in `app/main.py`
- Modular folders for `routers`, `services`, `models`, `core`, and `database`
- PostgreSQL connectivity via SQLAlchemy
- Environment variable loading from `.env`
- CORS middleware configured for a React frontend

## Project Structure

```text
app/
  core/
    config.py
  database/
    base.py
    session.py
  models/
    report.py
  routers/
    health.py
  services/
    health_service.py
  main.py
.env.example
pyproject.toml
```

## Run The App

1. Create a Python 3.11+ virtual environment.
2. Install dependencies:

```bash
pip install -e .
```

3. Copy the environment template and adjust values for your local PostgreSQL instance:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

4. Start the API server:

```bash
uvicorn app.main:app --reload
```

5. Open:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- Health check: `http://127.0.0.1:8000/api/v1/health`

## Environment Variables

- `APP_NAME`: FastAPI application name
- `API_PREFIX`: Base API prefix
- `DEBUG`: Debug mode flag
- `DATABASE_URL`: PostgreSQL SQLAlchemy connection string
- `CORS_ORIGINS`: Comma-separated frontend origins
