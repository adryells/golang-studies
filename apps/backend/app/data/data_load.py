from loguru import logger
from sqlalchemy.orm import Session

from apps.backend.app.data.individual import individuals_list
from apps.backend.app.data.individual.load import load_individuals
from apps.backend.app.data.individual_type import individual_types_list
from apps.backend.app.data.individual_type.load import load_individual_types
from apps.backend.app.database.session import main_session
from apps.backend.app.utils.breaker import only_in_development


def load_prod_data(session: Session):
    logger.info("Adding individual types...")
    load_individual_types(session=session, individuals_list=individual_types_list)


@only_in_development
def load_dev_data(session: Session):
    logger.info("Adding individual...")
    load_individuals(session=session, individuals_list=individuals_list)


def load_all(session: Session):
    load_prod_data(session=session)
    load_dev_data(session=session)


if __name__ == "__main__":
    db_session = main_session()
    load_all(session=db_session)
