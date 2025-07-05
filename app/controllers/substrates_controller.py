from app.models.substrate import Substrate
from app.db import get_session
from sqlmodel import select
from typing import List

def get_all_substrates() -> List[Substrate]:
    with get_session() as session:
        substrates = session.exec(select(Substrate)).all()
        return substrates

def add_substrate(substrate: Substrate) -> Substrate:
    with get_session() as session:
        session.add(substrate)
        session.commit()
        session.refresh(substrate)
        return substrate
