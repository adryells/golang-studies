from pydantic import BaseModel


class IndividualTypeData(BaseModel):
    name: str


pirate = IndividualTypeData(
    name="Pirate"
)

sailor = IndividualTypeData(
    name="Sailor"
)

govern_agent = IndividualTypeData(
    name="Govern Agent"
)

individual_types_list = [
    pirate, sailor, govern_agent
]
