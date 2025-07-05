from app.models.recipe import Step
from typing import List

steps: List[Step] = []

def get_all_steps() -> List[Step]:
    return steps

def add_step(step: Step) -> Step:
    steps.append(step)
    return step
