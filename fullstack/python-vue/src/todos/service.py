from sqlalchemy.orm import Session

from models import Todo, TodoCreate


def get(*, db_session: Session):
    """Gets the list of Todo's"""
    return db_session.query(Todo).all()


def create(*, db_session: Session, todo_in: TodoCreate):
    """Creates a new Todo"""
    todo = Todo(**todo_in.dict())

    db_session.add(todo)
    db_session.commit()
    return todo
