from sqlalchemy import Integer, Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from apps.backend.app.database.baseclass import Base
from apps.backend.app.models.mixins import TimeStampMixin


class Individual(Base, TimeStampMixin):
    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String, nullable=False)

    age = Column(Integer, nullable=False, default=0)

    active = Column(Boolean, nullable=False, default=True)

    individual_type_id = Column(Integer, ForeignKey("IndividualType.id"), nullable=False)
    individual_type = relationship("IndividualType")
