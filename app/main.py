from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.people import router as people_router

app = FastAPI()

# conexion con frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(people_router)

@app.get("/")
def root():
    return {"message": "API"}