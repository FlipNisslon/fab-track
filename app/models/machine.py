from typing import Optional
from sqlmodel import SQLModel, Field

class Machine(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    specifications: Optional[str] = None
