# Insight Engine

General-purpose data analytics app. Users view static reference data, input their own data, and get combined insights with visualizations. Domain-agnostic — adaptable to any use case.

## Stack

- **Frontend**: TypeScript, React 18, Tailwind CSS, Vite
- **Backend**: Python, FastAPI, SQLAlchemy 2.0, Alembic
- **Database**: PostgreSQL (local database named `myproject`)
- **Repo**: `git@github.com:Joshowens16/myProject.git`

## Project Structure

Currently the boilerplate starting point. See the parent `projects/CLAUDE.md` for boilerplate conventions (adding models, routes, pages, migrations).

```
myProject/
├── frontend/          # Vite + React + TypeScript + Tailwind
│   └── src/
│       ├── pages/     # Route-level components (currently just Home.tsx)
│       ├── components/# Reusable UI components (empty)
│       └── lib/
│           └── api.ts # Axios instance — use for all API calls
├── backend/           # FastAPI
│   ├── app/
│   │   ├── main.py    # App entry, CORS, route registration
│   │   ├── config.py  # Typed settings via pydantic-settings
│   │   ├── database.py# SQLAlchemy engine and get_db dependency
│   │   ├── models/    # SQLAlchemy models
│   │   └── routes/    # API routes (currently just api.py with /api/hello)
│   └── alembic/       # Database migrations
└── package.json       # Root — runs both servers with concurrently
```

## Running the App

```bash
npm run dev           # starts both frontend and backend
```

- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- API docs: http://localhost:8000/docs

## Development Approach

Building iteratively. Planned features (not yet implemented):

- **Static dataset system** — backend service to load/serve CSV/JSON reference data from `backend/app/data/`
- **Analysis engine** — backend service to combine user input with static data (pandas/numpy) and return insights
- **Dataset API** — `GET /api/datasets`, `GET /api/datasets/{id}`
- **Analysis API** — `POST /api/analyze` (user values + dataset → stats, comparisons, chart data)
- **Frontend pages** — Explore (browse datasets), Analyze (input form + results)
- **Frontend components** — Layout/nav, DataTable, ChartPanel (Recharts), InputForm
- **Git remote** — will change to `myPythonProject.git` when ready

## Database

- PostgreSQL running locally via Homebrew on port 5432
- Connection string in `backend/.env` (not committed)
- Default user is the system user (no password needed locally)

## Environment

- Backend env vars: `backend/.env` (see `backend/.env.example`)
- Frontend env vars: `VITE_` prefix (see `frontend/.env.example`)
- Dev proxy: Vite forwards `/api` requests to backend on port 8000
