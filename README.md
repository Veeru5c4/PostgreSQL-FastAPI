## Ecommerce Backend (FastAPI + PostgreSQL)

This is a starter backend for an ecommerce application built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

### Features

- **Users**: registration, login (JWT auth), basic profile
- **Inventory**: products and stock levels
- **Orders**: orders and order items
- **Payments**: simple payment record endpoint (integration-ready)

### Requirements

- Python 3.10+
- PostgreSQL 13+

### Setup

1. Create and activate a virtual environment:

```bash
cd /Users/veeraswamy/Desktop/Python-workplace/Ecommerce-Postgre
python -m venv .venv
source .venv/bin/activate  # on macOS/Linux
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure database URL (PostgreSQL):

Create a `.env` file in the project root:

```bash
echo "DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/ecommerce_db" > .env
echo "SECRET_KEY=change_me" >> .env
echo "ALGORITHM=HS256" >> .env
echo "ACCESS_TOKEN_EXPIRE_MINUTES=60" >> .env
```

Update `user`, `password`, and `ecommerce_db` according to your local PostgreSQL setup.

4. Run database migrations (create tables):

```bash
python -m app.init_db
```

5. Start the development server:

```bash
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs` in your browser for interactive API docs.


# PostgreSQL-FastAPI
