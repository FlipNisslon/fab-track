from fastapi import APIRouter
from app.models.machine import Machine
from typing import List

router = APIRouter()
machines: List[Machine] = []

@router.get("/machines", response_model=List[Machine])
def get_machines():
    return machines

@router.post("/machines", response_model=Machine)
def create_machine(machine: Machine):
    machines.append(machine)
    return machine
