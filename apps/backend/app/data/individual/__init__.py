from pydantic import BaseModel


class IndividualData(BaseModel):
    name: str
    age: int
    type_slug: str


luffy = IndividualData(
    name="Monkey D. Luffy",
    age=19,
    type_slug="pirate"
)

zoro = IndividualData(
    name="Roronoa Zoro",
    age=21,
    type_slug="pirate"
)

sanji = IndividualData(
    name="Vinsmoke Sanji",
    age=21,
    type_slug="pirate"
)

nami = IndividualData(
    name="Nami",
    age=20,
    type_slug="pirate"
)

usopp = IndividualData(
    name="Usopp",
    age=19,
    type_slug="pirate"
)


rob_lucci = IndividualData(
    name="Rob Lucci",
    age=30,
    type_slug="govern_agent"
)

kalifa = IndividualData(
    name="Kalifa",
    age=27,
    type_slug="govern_agent"
)

kaku = IndividualData(
    name="Kaku",
    age=25,
    type_slug="govern_agent"
)

akainu = IndividualData(
    name="Sakazuki Akainu",
    age=55,
    type_slug="sailor"
)

kizaru = IndividualData(
    name="Borsalino Kizaru",
    age=58,
    type_slug="sailor"
)

coby = IndividualData(
    name="Coby",
    age=18,
    type_slug="sailor"
)

garp = IndividualData(
    name="Monkey D. Garp",
    age=78,
    type_slug="sailor"
)

individuals_list = [
    garp, coby, kizaru, akainu, kaku, kalifa, rob_lucci, usopp, nami, sanji, zoro, luffy
]
