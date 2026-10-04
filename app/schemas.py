from pydantic import BaseModel
from typing import Optional

# Common fields shared across creation and reading
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None

# Schema for creating an item (Incoming request)
class TodoCreate(TodoBase):
    pass

# Schema for updating an item
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# Schema returned to the client (Outgoing response)
class TodoResponse(TodoBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True  # Instructs Pydantic to read SQLAlchemy ORM objects
