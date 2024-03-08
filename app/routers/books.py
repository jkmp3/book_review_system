from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.repositories import book_repository
from app.schemas.schemas import BookSchema, FilterSchema
from app.utils.db_utils import get_db_session

router = APIRouter()


@router.post("/books")
async def add_book(book: BookSchema,
                   db: Session = Depends(get_db_session)):
    book_repository.add_book(db, book)
    return {"message": "Book added successfully."}


@router.post("/get_books")
async def get_books(filter_schema: Optional[FilterSchema] = None,
                    db: Session = Depends(get_db_session)):
    if filter_schema is None:
        return {"books": book_repository.get_books(db)}

    books = book_repository.get_books(db,
                                      filter_schema.text_filter,
                                      filter_schema.range_filter)
    return {"books": books}


@router.get("/books/{book_id}")
async def get_book_by_id(book_id: int, db: Session = Depends(get_db_session)):
    return book_repository.get_book_by_id(db, book_id)
