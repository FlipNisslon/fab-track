from app.models.substrate import Interface
from typing import List

interfaces: List[Interface] = []

def get_all_interfaces() -> List[Interface]:
    return interfaces

def add_interface(interface: Interface) -> Interface:
    interfaces.append(interface)
    return interface
