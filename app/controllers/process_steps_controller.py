from app.models.recipe import ProcessStep
from typing import List

process_steps: List[ProcessStep] = []

def get_all_process_steps() -> List[ProcessStep]:
    return process_steps

def add_process_step(process_step: ProcessStep) -> ProcessStep:
    process_steps.append(process_step)
    return process_step
