from fastapi import APIRouter
from app.models.recipe import ProcessStep
from typing import List

router = APIRouter()
process_steps: List[ProcessStep] = []

@router.get("/process-steps", response_model=List[ProcessStep])
def get_process_steps():
    return process_steps

@router.post("/process-steps", response_model=ProcessStep)
def create_process_step(process_step: ProcessStep):
    process_steps.append(process_step)
    return process_step
