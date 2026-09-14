# Local Development Runbook

## Preferred baseline
- Git
- Docker Desktop
- Python 3.11+
- Node.js 20+ if dashboard uses Next.js
- Flutter SDK for mobile

Optional GIS tooling can be installed only for preprocessing.

## Environment
Create `.env` from `.env.example`. Never commit it.

Suggested variables:
```text
TRISHUL_ENV=development
TRISHUL_API_BASE_URL=http://localhost:8000
DEMO_MODE=true
WEATHER_BASE_URL=https://api.open-meteo.com
MODEL_PATH=
LOG_LEVEL=INFO
```

Start with the simplest runnable stack. Docker Compose may include backend and dashboard; do not require Postgres/Redis until they are actually needed.

## Verification
Backend: run tests and start FastAPI.
Dashboard: run development server and production build.
Mobile: run analyzer and Android build where available.

Always verify Demo Mode with external network disabled.
