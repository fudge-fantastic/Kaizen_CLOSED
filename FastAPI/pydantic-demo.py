from pydantic import BaseModel as PydanticBaseModel

data = {
    "name": "Aaditya",
    "age": "21",
    "alias": "Bluesalt",
    "ratings": [4, 4, "4", "5", 4]
}

# To ensure it's in the right format, we parse the data accordingly to obtain the right answer
class informative(PydanticBaseModel):
    name: str
    age: int
    alias: str
    ratings: list[int] = []

user = informative(**data)

print(f"Found the User: {user}")