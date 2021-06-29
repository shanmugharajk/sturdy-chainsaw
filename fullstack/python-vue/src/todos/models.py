from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import Boolean, String
from pydantic import BaseModel
from humps import camelize

from .database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    task = Column(String)
    is_active = Column(Boolean, default=False)


# dto's
def to_camel(string):
    return camelize(string)


class TodosBase(BaseModel):
    class Config:
        orm_mode = True
        validate_assignment = True
        alias_generator = to_camel
        allow_population_by_field_name = True


class TodoCreate(TodosBase):
    task: str


class TodoRead(TodosBase):
    task: str
    is_active: bool


class TodoUpdate(TodoRead):
    pass
