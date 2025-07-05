from app.models.recipe import Recipe, RecipeProcessStepLink, ProcessStep
from app.db import get_session
from sqlmodel import select
from typing import List

def get_all_recipes() -> List[Recipe]:
    with get_session() as session:
        recipes = session.exec(select(Recipe)).all()
        for recipe in recipes:
            # Sort process steps by order
            recipe.process_steps_links.sort(key=lambda link: link.order)
        return recipes

def add_recipe(recipe: Recipe, process_steps: List[int]) -> Recipe:
    with get_session() as session:
        session.add(recipe)
        session.commit()
        # Add process steps with order
        for idx, ps_id in enumerate(process_steps):
            link = RecipeProcessStepLink(recipe_id=recipe.id, process_step_id=ps_id, order=idx)
            session.add(link)
        session.commit()
        session.refresh(recipe)
        return recipe
