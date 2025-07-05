from typing import Optional
from sqlmodel import SQLModel, Field

class Substrate(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    material: str
    description: Optional[str] = None
    layers: Optional[str] = None  # Store as comma-separated string for simplicity

class Interface(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    affected_steps: Optional[str] = None  # Store as comma-separated string for simplicity
