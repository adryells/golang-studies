from loguru import logger

from apps.backend.app.data.data_load import load_all
from apps.backend.app.database.session import main_session
from apps.backend.app.database.utils import initialize_database, drop_database

db = main_session()


def main():
    drop_database(session=db)
    initialize_database(session=db)
    load_all(session=db)
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
