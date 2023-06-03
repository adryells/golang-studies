from sqlalchemy.orm import Session

from apps.backend.app.database.baseclass import Base


def initialize_database(session: Session):
    Base.metadata.create_all(bind=session.bind)


def drop_database(session: Session):
    Base.metadata.drop_all(bind=session.bind)
