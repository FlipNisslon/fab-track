from fastapi import APIRouter
from app.models.recipe import Recipe
from app.controllers.recipes_controller import get_all_recipes, add_recipe
from app.models.recipe import ProcessStep
from app.controllers.process_steps_controller import get_all_process_steps, add_process_step
from app.models.recipe import Step
from app.controllers.steps_controller import get_all_steps, add_step
from typing import List

router = APIRouter()

@router.get("/recipes", response_model=List[Recipe])
def get_recipes():
    return get_all_recipes()

@router.post("/recipes", response_model=Recipe)
def create_recipe(recipe: Recipe):
    return add_recipe(recipe)

@router.get("/process-steps", response_model=List[ProcessStep])
def get_process_steps():
    return get_all_process_steps()

@router.post("/process-steps", response_model=ProcessStep)
def create_process_step(process_step: ProcessStep):
    return add_process_step(process_step)

@router.get("/steps", response_model=List[Step])
def get_steps():
    return get_all_steps()

@router.post("/steps", response_model=Step)
def create_step(step: Step):
    return add_step(step)
