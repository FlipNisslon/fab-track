from typing import Optional
from sqlmodel import SQLModel, Field

class Step(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    temperature: Optional[float] = None
    pressure: Optional[float] = None
    duration: Optional[float] = None

class ProcessStep(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    # For simplicity, store step IDs as comma-separated string
    step_ids: Optional[str] = None

class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    # For simplicity, store process step IDs as comma-separated string
    process_step_ids: Optional[str] = None
