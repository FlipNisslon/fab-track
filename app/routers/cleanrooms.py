from fastapi import APIRouter
from app.models.cleanroom import Cleanroom
from app.controllers.cleanrooms_controller import get_all_cleanrooms, add_cleanroom
from typing import List

router = APIRouter()

@router.get("/cleanrooms", response_model=List[Cleanroom])
def get_cleanrooms():
    return get_all_cleanrooms()

@router.post("/cleanrooms", response_model=Cleanroom)
def create_cleanroom(cleanroom: Cleanroom):
    return add_cleanroom(cleanroom)
