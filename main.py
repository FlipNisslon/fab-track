from fastapi import FastAPI
from app.routers import recipes, cleanrooms, substrates, machines, process_steps, steps
from app.db import init_db


app = FastAPI()
init_db()


app.include_router(recipes.router)
app.include_router(cleanrooms.router)
app.include_router(substrates.router)
app.include_router(machines.router)
app.include_router(process_steps.router)
app.include_router(steps.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fabrication Engineering API"}
