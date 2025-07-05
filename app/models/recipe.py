from pydantic import BaseModel
from typing import List, Optional

class Step(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    temperature: Optional[float] = None
    pressure: Optional[float] = None
    duration: Optional[float] = None

class ProcessStep(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    steps: List[Step] = []

class Recipe(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    process_steps: List[ProcessStep] = []
