from loguru import logger
from sqlalchemy.orm import Session

from apps.backend.app.data.individual_type import IndividualTypeData
from apps.backend.app.models.individual.individual_type import IndividualType


def load_individual_types(session: Session, individuals_list: list[IndividualTypeData]):
    for individual_type_data in individuals_list:

        slug = individual_type_data.name.lower().replace(" ", "_")
        individual_type = session.query(
            session.query(IndividualType.id).filter(IndividualType.slug == slug).exists()
        ).scalar()

        if individual_type:
            logger.info(f"Individual type {slug} already exists. Skipping...")
            continue

        new_individual_type = IndividualType(
            name=individual_type_data.name,
            slug=slug
        )

        session.add(new_individual_type)
        session.commit()

        logger.success(f"Individual {new_individual_type.name} was added.")
