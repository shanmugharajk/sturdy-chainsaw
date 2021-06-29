from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import session
from database import get_db

from models import Todo, TodoCreate
from service import create, get

todos_router = APIRouter()


@todos_router.get("/todos")
def get_all_todos(db_session: session = Depends(get_db)) -> List[Todo]:
    return get(db_session=db_session)


@todos_router.post("/todos")
def create_todo(
    todo_in: TodoCreate,
    db_session: session = Depends(get_db),
) -> Todo:
    return create(db_session=db_session, todo_in=todo_in)
