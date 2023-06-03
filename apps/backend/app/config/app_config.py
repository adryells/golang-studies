import os
from random import choice

from pydantic import BaseSettings


class AppConfig(BaseSettings):
    CONFIG_NAME: str = 'TEST_DEV'

    DATABASE_URL: str = ''

    TESTING: bool = False

    DEVELOPMENT: bool = True

    class Config:
        env_file = "dev.env"
        env_prefix = "IAV_"


def get_config() -> AppConfig:
    if os.getenv("IAV_TESTING") == '1':
        random_str = "".join([choice("0123456789") for _ in range(10)])

        os.environ["IAV_DATABASE_URL"] = f'postgresql+psycopg2://user:senha123@127.0.0.1:5433/test_{random_str}'

        os.environ["IAV_CONFIG_NAME"] = "TEST"

        os.environ["IAV_DEVELOPMENT"] = "0"

    return AppConfig()


settings = get_config()
