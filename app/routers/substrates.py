from fastapi import APIRouter
from app.models.substrate import Substrate, Interface
from app.controllers.interfaces_controller import get_all_interfaces, add_interface
from typing import List

router = APIRouter()

substrates: List[Substrate] = []

@router.get("/substrates", response_model=List[Substrate])
def get_substrates():
    return substrates

@router.post("/substrates", response_model=Substrate)
def create_substrate(substrate: Substrate):
    substrates.append(substrate)
    return substrate

@router.get("/interfaces", response_model=List[Interface])
def get_interfaces():
    return get_all_interfaces()

@router.post("/interfaces", response_model=Interface)
def create_interface(interface: Interface):
    return add_interface(interface)
