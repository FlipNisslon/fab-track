from fastapi import APIRouter
from app.models.recipe import Step
from app.controllers.steps_controller import get_all_steps, add_step
from typing import List

router = APIRouter()

@router.get("/steps", response_model=List[Step])
def get_steps():
    return get_all_steps()

@router.post("/steps", response_model=Step)
def create_step(step: Step):
    return add_step(step)
