from functools import wraps

from apps.backend.app.config.app_config import settings


def only_in_development(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if settings.DEVELOPMENT:
            return func(*args, **kwargs)

    return decorator
