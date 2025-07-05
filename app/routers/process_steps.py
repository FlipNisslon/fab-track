from fastapi import APIRouter
from app.models.recipe import ProcessStep
from app.controllers.process_steps_controller import get_all_process_steps, add_process_step
from typing import List

router = APIRouter()

@router.get("/process-steps", response_model=List[ProcessStep])
def get_process_steps():
    return get_all_process_steps()

@router.post("/process-steps", response_model=ProcessStep)
def create_process_step(process_step: ProcessStep):
    return add_process_step(process_step)
