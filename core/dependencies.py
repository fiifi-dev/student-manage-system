from typing import Generator

from core.database import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def paginate_params(skip: int = 0, limit: int = 100):
    return {"skip": skip, "limit": limit}
