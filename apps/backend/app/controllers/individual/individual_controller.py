from fastapi import HTTPException

from apps.backend.app.controllers import BaseController
from apps.backend.app.models.individual.basic import Individual
from apps.backend.app.queries.individual_queries import IndividualQueries


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
