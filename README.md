# NovaCRM

NovaCRM is a CRM prototype with a FastAPI and SQLAlchemy backend, a React and Vite frontend, and Docker support for local Postgres and Redis services. The repository is useful as an application skeleton, but several product paths are still placeholders.

## Current implementation

The backend currently exposes:

- GET /health, which returns a simple status response.
- POST /auth/signup, which is a placeholder and currently returns a sample token value.
- GET /contacts, which currently returns an empty list.

The startup hook creates SQLAlchemy tables from the backend models. The README and directory layout describe contact management, pipeline tracking, and collaboration as the intended product areas; implement and test those flows before treating them as complete features.

## Repository layout

- backend/main.py is the FastAPI entry point.
- backend/app contains application models and supporting code.
- backend/migrations and backend/tests are reserved for schema changes and tests.
- backend/requirements.txt lists the Python dependencies.
- backend/.env.example documents database, Stripe, SMTP, and JWT settings.
- frontend contains the React and Vite client.
- infra/docker/docker-compose.yml defines Postgres, Redis, backend, and frontend services.
- docs contains architecture records, incidents, and meeting notes.

## Local development

### Backend

~~~bash
cd backend
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
~~~

The API is available at http://127.0.0.1:8000 and the health check is at /health. FastAPI exposes interactive documentation at /docs while the server is running.

### Frontend

~~~bash
cd frontend
npm install
npm run dev
~~~

Vite prints the local frontend URL. Configure the client API base URL to point at the backend when wiring new screens.

### Docker services

From the repository root:

~~~bash
docker compose -f infra/docker/docker-compose.yml up --build
~~~

The compose file provisions Postgres on port 5432, Redis on port 6379, the backend on port 8000, and the frontend on port 5173. The current backend entry point defaults to a local SQLite URL, so align the application configuration with the compose environment before relying on Postgres or Redis in a deployed environment.

## Configuration and security

Copy backend/.env.example to an environment-specific file and replace every placeholder. Never commit Stripe keys, SMTP passwords, JWT secrets, database credentials, or other sensitive values. Review authentication, authorization, input validation, migrations, and CORS settings before exposing the API.

## Testing

The backend requirements include pytest. Add focused tests for authentication, contacts, persistence, and API error cases as those features are implemented. Run the backend test suite from the backend directory with pytest.

## Status

NovaCRM is an active prototype rather than a production CRM. The documented architecture is broader than the current endpoint implementations, and the placeholder auth and contacts routes need real persistence and security work before production use.
