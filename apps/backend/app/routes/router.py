from fastapi import APIRouter

from apps.backend.app.routes.individual import individual_router
from apps.backend.app.routes.individual_type import individual_type_router

api_router = APIRouter(
    prefix="/api"
)

api_router.include_router(individual_router)
api_router.include_router(individual_type_router)
