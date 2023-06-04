from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.backend.app.controllers.individual.individual_controller import IndividualController
from apps.backend.app.database.session import main_session
from apps.backend.app.dto.individual_model import CreateIndividualData, UpdateIndividualData

individual_router = APIRouter(prefix="/individual")


@individual_router.get("/{individual_id}")
def get_individual_by_id(individual_id: int, session: Session = Depends(main_session)):
    indvidual = IndividualController(session).get_individual_by_id(individual_id)

    return {"result": indvidual}


@individual_router.get("/")
def get_all_individuals(page: int = None, per_page: int = None, session: Session = Depends(main_session)):
    individuals = IndividualController(session=session).get_individuals(page=page, per_page=per_page)

    return {"result": individuals}


@individual_router.post("/add")
def add_individual(data: CreateIndividualData, session: Session = Depends(main_session)):
    IndividualController(session).create_individual(data=data)

    return {"result": "new individual was added."}


@individual_router.put("/update/{individual_id}")
def update_individual(individual_id: int, data: UpdateIndividualData, session: Session = Depends(main_session)):
    IndividualController(session).update_individual(individual_id=individual_id, data=data)

    return {"result": f"{individual_id} has been updated."}


@individual_router.delete("/delete/{individual_id}")
def delete_individual(individual_id: int, session: Session = Depends(main_session)):
    IndividualController(session).delete_individual(individual_id=individual_id)

    return {"result": f"{individual_id} has been deleted."}
