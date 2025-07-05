from app.models.machine import Machine
from app.db import get_session
from sqlmodel import select
from typing import List

def get_all_machines() -> List[Machine]:
    with get_session() as session:
        machines = session.exec(select(Machine)).all()
        return machines

def add_machine(machine: Machine) -> Machine:
    with get_session() as session:
        session.add(machine)
        session.commit()
        session.refresh(machine)
        return machine
