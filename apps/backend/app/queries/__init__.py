from typing import Type

from sqlalchemy.orm import Session, Query

from apps.backend.app.database.baseclass import Base


class BaseQueries:
    def __init__(self, session: Session):
        self.session = session

    def get_one_or_none_by_id(self, object_model: Type[Base], object_id: int) -> Type[Base]:
        query = self.session.query(object_model).filter(object_model.id == object_id)

        return query.one_or_none()

    def get_query_with_pagination(self, query: Query, page: int = None, per_page: int = None) -> Query:
        query = query.limit(per_page).offset((page - 1) * per_page)

        return query

