from pydantic import BaseModel
from typing import List, Optional

class Machine(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    specifications: Optional[str] = None
    process_step_ids: List[str] = []

class Cleanroom(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    machines: List[Machine] = []
