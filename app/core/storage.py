import json
from typing import List
from app.schemas.person import Person

FILE_PATH = 'people.json'

def read_people() -> List[Person]:
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Person(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write_people(people: List[Person]):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump([person.dict() for person in people], file, indent=2)