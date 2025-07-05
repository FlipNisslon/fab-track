from app.models.cleanroom import Cleanroom
from app.db import get_session
from sqlmodel import select
from typing import List

def get_all_cleanrooms() -> List[Cleanroom]:
    with get_session() as session:
        cleanrooms = session.exec(select(Cleanroom)).all()
        return cleanrooms

def add_cleanroom(cleanroom: Cleanroom) -> Cleanroom:
    with get_session() as session:
        session.add(cleanroom)
        session.commit()
        session.refresh(cleanroom)
        return cleanroom
