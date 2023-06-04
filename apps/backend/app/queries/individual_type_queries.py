from typing import Optional

from apps.backend.app.models.individual.individual_type import IndividualType
from apps.backend.app.queries import BaseQueries


class IndividualTypeQueries(BaseQueries):
    def get_individual_type_by_id(self, individual_type_id: int) -> Optional[IndividualType]:
        individual_type = self.get_one_or_none_by_id(IndividualType, individual_type_id)

        return individual_type

    def get_individual_types(self, page: int = None, per_page: int = None) -> list[IndividualType]:
        query = self.session.query(IndividualType)

        if page and per_page:
            query = self.get_query_with_pagination(query=query, page=page, per_page=per_page)

        return query.all()
