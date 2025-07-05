from app.models.recipe import Recipe
from app.db import get_session
from sqlmodel import select
from typing import List

def get_all_recipes() -> List[Recipe]:
    with get_session() as session:
        recipes = session.exec(select(Recipe)).all()
        return recipes

def add_recipe(recipe: Recipe) -> Recipe:
    with get_session() as session:
        session.add(recipe)
        session.commit()
        session.refresh(recipe)
        return recipe
