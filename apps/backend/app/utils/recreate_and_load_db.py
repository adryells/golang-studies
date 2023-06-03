from loguru import logger

from apps.backend.app.data.data_load import load_all
from apps.backend.app.database.session import main_session
from apps.backend.app.database.utils import initialize_database, drop_database

db = main_session()


def init() -> None:
    initialize_database(db)
    load_all(session=db)


def main() -> None:
    drop_database(session=db)
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
