from fastapi import APIRouter
from app.models.recipe import Step
from typing import List

router = APIRouter()
steps: List[Step] = []

@router.get("/steps", response_model=List[Step])
def get_steps():
    return steps

@router.post("/steps", response_model=Step)
def create_step(step: Step):
    steps.append(step)
    return step
