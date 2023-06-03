from loguru import logger
from sqlalchemy.orm import Session

from apps.backend.app.data.individual import IndividualData
from apps.backend.app.models.individual.basic import Individual
from apps.backend.app.models.individual.individual_type import IndividualType


def load_individuals(session: Session, individuals_list: list[IndividualData]):
    for individual_data in individuals_list:
        individual_type = session.query(IndividualType)\
            .filter(IndividualType.slug == individual_data.type_slug).one_or_none()

        new_individual = Individual(
            name=individual_data.name,
            age=individual_data.age,
            individual_type=individual_type
        )

        session.add(new_individual)
        session.commit()

        logger.success(f"Individual {new_individual.name} was added.")
