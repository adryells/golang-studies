from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.backend.app.controllers.individual_type.individual_type_controller import IndividualTypeController
from apps.backend.app.database.session import main_session
from apps.backend.app.dto.individual_type_models import CreateIndividualTypeData, UpdateIndividualTypeData

individual_type_router = APIRouter(
    prefix="/individual_type"
)


@individual_type_router.get("/{individual_type_id}")
def get_individual_type_by_id(individual_type_id: int, session: Session = Depends(main_session)):
    individual_type = IndividualTypeController(session).get_individual_type_by_id(individual_type_id=individual_type_id)

    return {"result": individual_type}


@individual_type_router.get("/")
def get_all_individual_types(page: int = None, per_page: int = None, session: Session = Depends(main_session)):
    individual_types = IndividualTypeController(session).get_individual_types(page=page, per_page=per_page)

    return {"result": individual_types}


@individual_type_router.post("/add")
def add_individual_type(data: CreateIndividualTypeData, session: Session = Depends(main_session)):
    IndividualTypeController(session).create_individual_type(data=data)

    return {"result": "new individual type was added."}


@individual_type_router.put("/update/{individual_type_id}")
def update_individual_type(
        data: UpdateIndividualTypeData,
        individual_type_id: int,
        session: Session = Depends(main_session)
):
    IndividualTypeController(session).update_individual_type(data=data, individual_type_id=individual_type_id)

    return {"result": f"Individual type ID: {individual_type_id} has been updated."}


@individual_type_router.delete("/delete/{individual_type_id}")
def delete_individual_type(individual_type_id: int, session: Session = Depends(main_session)):
    IndividualTypeController(session).delete_individual_type(individual_type_id=individual_type_id)

    return {"result": f"Individual type ID: {individual_type_id} has been deleted."}
