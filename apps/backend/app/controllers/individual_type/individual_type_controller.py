from fastapi import HTTPException

from apps.backend.app.controllers import BaseController
from apps.backend.app.models.individual.individual_type import IndividualType
from apps.backend.app.queries.individual_type_queries import IndividualTypeQueries


class IndividualTypeController(BaseController):
    def get_individual_type_by_id(self, individual_type_id: int) -> IndividualType:
        individual_type = IndividualTypeQueries(self.session).get_individual_type_by_id(
            individual_type_id=individual_type_id
        )

        if not individual_type:
            raise HTTPException(status_code=404, detail="Individual type not found.")

        return individual_type

    def _validate_individual_types_filters(self, page: int = None, per_page: int = None):
        if (page is not None and per_page is not None) and (page < 1 or per_page < 1):
            raise HTTPException(status_code=400, detail="Invalid pagination params.")

    def get_individual_types(self, page: int = None, per_page: int = None) -> list[IndividualType]:
        self._validate_individual_types_filters(page=page, per_page=per_page)

        individual_types = IndividualTypeQueries(self.session).get_individual_types(page=page, per_page=per_page)

        return individual_types
