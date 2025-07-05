from app.models.machine import Machine
from typing import List

machines: List[Machine] = []

def get_all_machines() -> List[Machine]:
    return machines

def add_machine(machine: Machine) -> Machine:
    machines.append(machine)
    return machine
