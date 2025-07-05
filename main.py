from fastapi import FastAPI
from app.routers import recipes, cleanrooms, substrates

app = FastAPI()

app.include_router(recipes.router)
app.include_router(cleanrooms.router)
app.include_router(substrates.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fabrication Engineering API"}
