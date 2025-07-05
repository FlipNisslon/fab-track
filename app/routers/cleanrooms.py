from fastapi import APIRouter, HTTPException
from app.models.cleanroom import Cleanroom
from app.controllers.cleanrooms_controller import get_all_cleanrooms, add_cleanroom
from app.db import get_session
from sqlmodel import select
from typing import List

router = APIRouter()

@router.get("/cleanrooms", response_model=List[Cleanroom])
def get_cleanrooms():
    return get_all_cleanrooms()

@router.post("/cleanrooms", response_model=Cleanroom)
def create_cleanroom(cleanroom: Cleanroom):
    return add_cleanroom(cleanroom)

@router.put("/cleanrooms/{cleanroom_id}", response_model=Cleanroom)
def update_cleanroom(cleanroom_id: int, cleanroom: Cleanroom):
    with get_session() as session:
        db_cleanroom = session.get(Cleanroom, cleanroom_id)
        if not db_cleanroom:
            raise HTTPException(status_code=404, detail="Cleanroom not found")
        for field, value in cleanroom.dict(exclude_unset=True).items():
            setattr(db_cleanroom, field, value)
        session.add(db_cleanroom)
        session.commit()
        session.refresh(db_cleanroom)
        return db_cleanroom

@router.delete("/cleanrooms/{cleanroom_id}", response_model=Cleanroom)
def delete_cleanroom(cleanroom_id: int):
    with get_session() as session:
        db_cleanroom = session.get(Cleanroom, cleanroom_id)
        if not db_cleanroom:
            raise HTTPException(status_code=404, detail="Cleanroom not found")
        session.delete(db_cleanroom)
        session.commit()
        return db_cleanroom
