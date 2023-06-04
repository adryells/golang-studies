from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, validator


class CreateIndividualTypeData(BaseModel):
    name: str

    @validator("name")
    def validate_name_length(cls, name: str):
        if len(name) < 2:
            raise HTTPException(status_code=400, detail="Invalid name length, must pass a minimum of 2 chars.")

        return name


class UpdateIndividualTypeData(BaseModel):
    name: Optional[str]

    @validator("name")
    def validate_name_length(cls, name: str):
        if name and len(name) < 2:
            raise HTTPException(status_code=400, detail="Invalid name length, must pass a minimum of 2 chars.")

        return name
