from fastapi import APIRouter, Depends, HTTPException
from app.models.machine import Machine
from app.controllers.machines_controller import get_all_machines, add_machine
from app.db import get_session
from sqlmodel import select
from typing import List

router = APIRouter()

@router.get("/machines", response_model=List[Machine])
def get_machines():
    return get_all_machines()

@router.post("/machines", response_model=Machine)
def create_machine(machine: Machine):
    return add_machine(machine)

@router.put("/machines/{machine_id}", response_model=Machine)
def update_machine(machine_id: int, machine: Machine):
    with get_session() as session:
        db_machine = session.get(Machine, machine_id)
        if not db_machine:
            raise HTTPException(status_code=404, detail="Machine not found")
        for field, value in machine.dict(exclude_unset=True).items():
            setattr(db_machine, field, value)
        session.add(db_machine)
        session.commit()
        session.refresh(db_machine)
        return db_machine

@router.delete("/machines/{machine_id}", response_model=Machine)
def delete_machine(machine_id: int):
    with get_session() as session:
        db_machine = session.get(Machine, machine_id)
        if not db_machine:
            raise HTTPException(status_code=404, detail="Machine not found")
        session.delete(db_machine)
        session.commit()
        return db_machine
