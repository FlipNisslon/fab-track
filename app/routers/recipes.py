from fastapi import APIRouter
from app.models.recipe import Recipe
from typing import List

router = APIRouter()

# In-memory storage for demonstration
recipes: List[Recipe] = []

@router.get("/recipes", response_model=List[Recipe])
def get_recipes():
    return recipes

@router.post("/recipes", response_model=Recipe)
def create_recipe(recipe: Recipe):
    recipes.append(recipe)
    return recipe
