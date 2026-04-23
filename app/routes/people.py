from fastapi import APIRouter, HTTPException
from app.schemas.person import Person
from app.core.storage import read_people, write_people

router = APIRouter()


@router.get("/getPeople")
def get_people():
    return read_people()


@router.post("/addPerson")
def add_person(person: Person):
    people = read_people()

    # Validar duplicados
    if any(p.email == person.email for p in people):
        raise HTTPException(status_code=400, detail="Correo electronico ya existe")

    people.append(person)
    write_people(people)

    return {"message": "Persona agregada correctamente"}