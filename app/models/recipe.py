from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .process_step import ProcessStep

class Step(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    temperature: Optional[float] = None
    pressure: Optional[float] = None
    duration: Optional[float] = None


class RecipeProcessStepLink(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    recipe_id: int = Field(foreign_key="recipe.id")
    process_step_id: int = Field(foreign_key="processstep.id")
    order: int
    recipe: Optional["Recipe"] = Relationship(back_populates="process_steps_links")
    process_step: Optional["ProcessStep"] = Relationship(back_populates="recipes_links")

class ProcessStep(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    # Relationship to RecipeProcessStepLink
    recipes_links: List["RecipeProcessStepLink"] = Relationship(back_populates="process_step")

class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    # Relationship to RecipeProcessStepLink
    process_steps_links: List["RecipeProcessStepLink"] = Relationship(back_populates="recipe")
