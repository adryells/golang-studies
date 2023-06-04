from fastapi import HTTPException

from apps.backend.app.controllers import BaseController
from apps.backend.app.dto.individual_model import UpdateIndividualData, CreateIndividualData
from apps.backend.app.models.individual.basic import Individual
from apps.backend.app.queries.individual_queries import IndividualQueries
from apps.backend.app.queries.individual_type_queries import IndividualTypeQueries


class IndividualController(BaseController):
    def get_individual_by_id(self, individual_id: int) -> Individual:
        individual = IndividualQueries(self.session).get_individual_by_id(individual_id=individual_id)

        if not individual:
            raise HTTPException(status_code=404, detail="Individual not found.")

        return individual

    def _validate_individuals_params(self, page: int = None, per_page: int = None):
        if (page is not None and per_page is not None) and (page < 1 or per_page < 1):
            raise HTTPException(status_code=400, detail="Invalid pagination params.")

    def get_individuals(self, page: int = None, per_page: int = None) -> list[Individual]:
        self._validate_individuals_params(page=page, per_page=per_page)

        individuals = IndividualQueries(self.session).get_individuals(page=page, per_page=per_page)

        return individuals

    def create_individual(self, data: CreateIndividualData):
        individual_type = IndividualTypeQueries(self.session).get_individual_type_by_id(data.individual_type_id)

        if not individual_type:
            raise HTTPException(status_code=404, detail="Individual type not found.")

        new_individual = Individual(
            name=data.name,
            age=data.age,
            individual_type=individual_type
        )

        self.session.add(new_individual)
        self.session.commit()

    def _update_type_from_a_individual(self, individual: Individual, individual_type_id: int):
        individual_type = IndividualTypeQueries(self.session).get_individual_type_by_id(individual_type_id)

        if not individual_type:
            raise HTTPException(status_code=404, detail="Individual type not found.")

        individual.individual_type = individual_type

    def update_individual(self, individual_id: int, data: UpdateIndividualData):
        individual = self.get_individual_by_id(individual_id=individual_id)

        handler = {
            "name": lambda: setattr(individual, "name", data.name),
            "age": lambda: setattr(individual, "age", data.age),
            "individual_type_id": lambda: self._update_type_from_a_individual(individual, data.individual_type_id)
        }

        for key, value in data.__dict__.items():
            if value:
                handler[key]()

        self.session.commit()

    def delete_individual(self, individual_id: int):
        individual = self.get_individual_by_id(individual_id=individual_id)

        individual.active = False

        self.session.commit()
