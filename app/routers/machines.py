from fastapi import APIRouter, Depends
from app.models.machine import Machine
from app.controllers.machines_controller import get_all_machines, add_machine
from typing import List

router = APIRouter()

@router.get("/machines", response_model=List[Machine])
def get_machines():
    return get_all_machines()

@router.post("/machines", response_model=Machine)
def create_machine(machine: Machine):
    return add_machine(machine)
