from pydantic import BaseModel
from typing import List, Optional

class Substrate(BaseModel):
    id: str
    material: str
    description: Optional[str] = None
    layers: List[str] = []

class Interface(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    affected_steps: List[str] = []
