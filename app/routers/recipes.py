from fastapi import APIRouter, HTTPException
from app.models.recipe import Recipe, ProcessStep, Step, RecipeProcessStepLink
from app.controllers.recipes_controller import get_all_recipes, add_recipe
from app.controllers.process_steps_controller import get_all_process_steps, add_process_step
from app.controllers.steps_controller import get_all_steps, add_step
from app.db import get_session
from sqlmodel import select
from typing import List

router = APIRouter()

@router.get("/recipes", response_model=List[Recipe])
def get_recipes():
    return get_all_recipes()

@router.post("/recipes", response_model=Recipe)
def create_recipe(recipe: Recipe, process_steps: List[int]):
    return add_recipe(recipe, process_steps)

@router.put("/recipes/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: Recipe):
    with get_session() as session:
        db_recipe = session.get(Recipe, recipe_id)
        if not db_recipe:
            raise HTTPException(status_code=404, detail="Recipe not found")
        for field, value in recipe.dict(exclude_unset=True).items():
            setattr(db_recipe, field, value)
        session.add(db_recipe)
        session.commit()
        session.refresh(db_recipe)
        return db_recipe

@router.delete("/recipes/{recipe_id}", response_model=Recipe)
def delete_recipe(recipe_id: int):
    with get_session() as session:
        db_recipe = session.get(Recipe, recipe_id)
        if not db_recipe:
            raise HTTPException(status_code=404, detail="Recipe not found")
        session.delete(db_recipe)
        session.commit()
        return db_recipe

@router.get("/process-steps", response_model=List[ProcessStep])
def get_process_steps():
    return get_all_process_steps()

@router.post("/process-steps", response_model=ProcessStep)
def create_process_step(process_step: ProcessStep):
    return add_process_step(process_step)

@router.put("/process-steps/{process_step_id}", response_model=ProcessStep)
def update_process_step(process_step_id: int, process_step: ProcessStep):
    with get_session() as session:
        db_process_step = session.get(ProcessStep, process_step_id)
        if not db_process_step:
            raise HTTPException(status_code=404, detail="ProcessStep not found")
        for field, value in process_step.dict(exclude_unset=True).items():
            setattr(db_process_step, field, value)
        session.add(db_process_step)
        session.commit()
        session.refresh(db_process_step)
        return db_process_step

@router.delete("/process-steps/{process_step_id}", response_model=ProcessStep)
def delete_process_step(process_step_id: int):
    with get_session() as session:
        db_process_step = session.get(ProcessStep, process_step_id)
        if not db_process_step:
            raise HTTPException(status_code=404, detail="ProcessStep not found")
        session.delete(db_process_step)
        session.commit()
        return db_process_step

@router.get("/steps", response_model=List[Step])
def get_steps():
    return get_all_steps()

@router.post("/steps", response_model=Step)
def create_step(step: Step):
    return add_step(step)

@router.put("/steps/{step_id}", response_model=Step)
def update_step(step_id: int, step: Step):
    with get_session() as session:
        db_step = session.get(Step, step_id)
        if not db_step:
            raise HTTPException(status_code=404, detail="Step not found")
        for field, value in step.dict(exclude_unset=True).items():
            setattr(db_step, field, value)
        session.add(db_step)
        session.commit()
        session.refresh(db_step)
        return db_step

@router.delete("/steps/{step_id}", response_model=Step)
def delete_step(step_id: int):
    with get_session() as session:
        db_step = session.get(Step, step_id)
        if not db_step:
            raise HTTPException(status_code=404, detail="Step not found")
        session.delete(db_step)
        session.commit()
        return db_step
