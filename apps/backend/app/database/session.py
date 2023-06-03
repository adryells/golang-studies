from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy.pool import NullPool

from apps.backend.app.config.app_config import settings

engine = create_engine(url=settings.DATABASE_URL, poolclass=NullPool)

SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))


def get_session() -> Iterator[Session]:
    session = SessionLocal()

    yield session

    session.close()


def main_session() -> Session:
    return next(get_session())
