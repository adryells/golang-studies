from sqlalchemy import Column, Integer, String, Boolean

from apps.backend.app.database.baseclass import Base
from apps.backend.app.models.mixins import TimeStampMixin


class IndividualType(Base, TimeStampMixin):
    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String, nullable=False)

    slug = Column(String, nullable=False, unique=True)

    active = Column(Boolean, nullable=False, default=True)
