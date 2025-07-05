from app.models.substrate import Interface
from app.db import get_session
from sqlmodel import select
from typing import List

def get_all_interfaces() -> List[Interface]:
    with get_session() as session:
        interfaces = session.exec(select(Interface)).all()
        return interfaces

def add_interface(interface: Interface) -> Interface:
    with get_session() as session:
        session.add(interface)
        session.commit()
        session.refresh(interface)
        return interface
