from app.models.recipe import Step
from app.db import get_session
from sqlmodel import select
from typing import List

def get_all_steps() -> List[Step]:
    with get_session() as session:
        steps = session.exec(select(Step)).all()
        return steps

def add_step(step: Step) -> Step:
    with get_session() as session:
        session.add(step)
        session.commit()
        session.refresh(step)
        return step
