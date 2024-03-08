from typing import Optional, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.enums.error_codes import ErrorCodes
from app.repositories import book_repository
from app.schemas.request_schemas import BookSchema, FilterSchema
from app.schemas.response_schemas import BadRequestResponse, OkayResponse, PaginatedResponse
from app.utils.db_utils import get_db_session

router = APIRouter()


@router.post("/books")
def add_book(book: BookSchema,
             db: Session = Depends(get_db_session)):
    """

    Args:
        book: book instance with the data to be saved
        db: database session object

    Returns:
        returns the saved object, if duplicate throws error
    """
    try:
        book = book_repository.add_book(db, book)
    except ValueError:
        return BadRequestResponse(code=ErrorCodes.BOOK_ALREADY_EXISTS.error_id,
                                  message=ErrorCodes.BOOK_ALREADY_EXISTS.message).dict()
    return OkayResponse(code=200, result=book).dict()


@router.post("/get_books")
def get_books(limit: int = 10,
              offset: int = 0,
              filter_schema: Optional[FilterSchema] = None,
              db: Session = Depends(get_db_session)):
    """
    Returns the list of books
    Args:
        limit: number of items per page
        offset: results will start from this index (index start from 0)
        filter_schema: can contain text and range filter operations
        db: database session object

    Returns:
        paginated list of books
    """
    if filter_schema is None:
        books = book_repository.get_books(db, limit, offset)
        return PaginatedResponse(code=200, limit=limit, offset=offset, result=books).dict()

    books = book_repository.get_books(db,
                                      limit,
                                      offset,
                                      filter_schema.text_filter,
                                      filter_schema.range_filter)
    return PaginatedResponse(code=200, limit=limit, offset=offset, result=books).dict()


@router.get("/books/{book_id}")
def get_book_by_id(book_id: int, db: Session = Depends(get_db_session)) -> dict[str, Any]:
    """
    Returns the info on book with the given id
    Args:
        book_id: id of the book
        db: database session object

    Returns:
        Returns the book, or error response if book with id does not exist
    """
    book = book_repository.get_book_by_id(db, book_id)
    if book is None:
        return BadRequestResponse(code=ErrorCodes.BOOK_DOES_NOT_EXIST.error_id,
                                  message=ErrorCodes.BOOK_DOES_NOT_EXIST.message).dict()
    return book
