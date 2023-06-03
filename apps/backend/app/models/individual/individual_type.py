from sqlalchemy import Column, Integer, String

from apps.backend.app.database.baseclass import Base


class IndividualType(Base):
    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String, nullable=False)

    slug = Column(String, nullable=False, unique=True)
