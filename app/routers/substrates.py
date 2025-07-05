from fastapi import APIRouter, HTTPException
from app.models.substrate import Substrate, Interface
from app.controllers.substrates_controller import get_all_substrates, add_substrate
from app.controllers.interfaces_controller import get_all_interfaces, add_interface
from app.db import get_session
from sqlmodel import select
from typing import List

router = APIRouter()

@router.get("/substrates", response_model=List[Substrate])
def get_substrates():
    return get_all_substrates()

@router.post("/substrates", response_model=Substrate)
def create_substrate(substrate: Substrate):
    return add_substrate(substrate)

@router.put("/substrates/{substrate_id}", response_model=Substrate)
def update_substrate(substrate_id: int, substrate: Substrate):
    with get_session() as session:
        db_substrate = session.get(Substrate, substrate_id)
        if not db_substrate:
            raise HTTPException(status_code=404, detail="Substrate not found")
        for field, value in substrate.dict(exclude_unset=True).items():
            setattr(db_substrate, field, value)
        session.add(db_substrate)
        session.commit()
        session.refresh(db_substrate)
        return db_substrate

@router.delete("/substrates/{substrate_id}", response_model=Substrate)
def delete_substrate(substrate_id: int):
    with get_session() as session:
        db_substrate = session.get(Substrate, substrate_id)
        if not db_substrate:
            raise HTTPException(status_code=404, detail="Substrate not found")
        session.delete(db_substrate)
        session.commit()
        return db_substrate

@router.get("/interfaces", response_model=List[Interface])
def get_interfaces():
    return get_all_interfaces()

@router.post("/interfaces", response_model=Interface)
def create_interface(interface: Interface):
    return add_interface(interface)

@router.put("/interfaces/{interface_id}", response_model=Interface)
def update_interface(interface_id: int, interface: Interface):
    with get_session() as session:
        db_interface = session.get(Interface, interface_id)
        if not db_interface:
            raise HTTPException(status_code=404, detail="Interface not found")
        for field, value in interface.dict(exclude_unset=True).items():
            setattr(db_interface, field, value)
        session.add(db_interface)
        session.commit()
        session.refresh(db_interface)
        return db_interface

@router.delete("/interfaces/{interface_id}", response_model=Interface)
def delete_interface(interface_id: int):
    with get_session() as session:
        db_interface = session.get(Interface, interface_id)
        if not db_interface:
            raise HTTPException(status_code=404, detail="Interface not found")
        session.delete(db_interface)
        session.commit()
        return db_interface
