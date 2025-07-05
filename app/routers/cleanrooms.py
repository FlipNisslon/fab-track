from fastapi import APIRouter
from app.models.cleanroom import Cleanroom
from typing import List

router = APIRouter()

cleanrooms: List[Cleanroom] = []

@router.get("/cleanrooms", response_model=List[Cleanroom])
def get_cleanrooms():
    return cleanrooms

@router.post("/cleanrooms", response_model=Cleanroom)
def create_cleanroom(cleanroom: Cleanroom):
    cleanrooms.append(cleanroom)
    return cleanroom
