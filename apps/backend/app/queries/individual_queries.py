from typing import Optional

from apps.backend.app.models.individual.basic import Individual
from apps.backend.app.queries import BaseQueries


class IndividualQueries(BaseQueries):
    def get_individual_by_id(self, individual_id: int) -> Optional[Individual]:
        individual = self.get_one_or_none_by_id(Individual, individual_id)

        return individual

    def get_individuals(self, page: int = None, per_page: int = None) -> list[Individual]:
        query = self.session.query(Individual)

        if page and per_page:
            query = self.get_query_with_pagination(query=query, page=page, per_page=per_page)

        return query.all()
