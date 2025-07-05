from app.models.recipe import ProcessStep
from app.db import get_session
from sqlmodel import select
from typing import List

def get_all_process_steps() -> List[ProcessStep]:
    with get_session() as session:
        process_steps = session.exec(select(ProcessStep)).all()
        return process_steps

def add_process_step(process_step: ProcessStep) -> ProcessStep:
    with get_session() as session:
        session.add(process_step)
        session.commit()
        session.refresh(process_step)
        return process_step
