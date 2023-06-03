from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from apps.backend.app.database.baseclass import Base


class Individual(Base):
    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String, nullable=False)

    age = Column(Integer, nullable=False, default=0)

    individual_type_id = Column(Integer, ForeignKey("IndividualType.id"), nullable=False)
    individual_type = relationship("IndividualType")

