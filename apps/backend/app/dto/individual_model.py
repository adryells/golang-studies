from typing import Optional

from pydantic import BaseModel


class CreateIndividualData(BaseModel):
    name: str
    age: int
    individual_type_id: int


class UpdateIndividualData(BaseModel):
    name: Optional[str]
    age: Optional[int]
    individual_type_id: Optional[int]
