"""Database operations related to book entity"""

from typing import Optional, Type

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.enums.error_codes import ErrorCodes
from app.enums.string_comparison import StringComparison
from app.models.models import Book
from app.schemas.request_schemas import BookSchema, TextFilterSchema, RangeFilterSchema


def get_books(db: Session,
              text_filter: Optional[TextFilterSchema] = None,
              range_filter: Optional[RangeFilterSchema] = None) -> list[Type[Book]]:
    """
    Get the list of information about all the books that satisfy the filter conditions (if any)
    Args:
        db: database session object
        text_filter: filter object for string comparisons for string columns
        range_filter: filter object for applying numeric range operations for integer columns

    Returns:
        List of book objects
    """
    query = db.query(Book)

    if hasattr(text_filter, "field") and text_filter.field == "author_name":
        if text_filter.operation == StringComparison.EQUALS:
            query = query.filter(Book.author_name == text_filter.text)
        elif text_filter.operation == StringComparison.EQUALS_IGNORE_CASE:
            query = query.filter(Book.author_name.ilike(text_filter.text))
        elif text_filter.operation == StringComparison.CONTAINS:
            query = query.filter(Book.author_name.contains(text_filter.text))
        elif text_filter.operation == StringComparison.CONTAINS_IGNORE_CASE:
            query = query.filter(Book.author_name.icontains(text_filter.text))

    if hasattr(range_filter, "field") and range_filter.field == "publication_year":
        query = query.filter(Book.publication_year.between(range_filter.lower_bound, range_filter.upper_bound))
    return query.all()


def get_book_by_id(db: Session, book_id: int) -> Optional[Book]:
    """
    Get the information on the book with the specified id
    Args:
        db: database session object
        book_id: id of the book

    Returns:
        attribute and attribute values of the specified book
    """
    return db.query(Book).filter(Book.id == book_id).first()


def add_book(db: Session, book: BookSchema) -> Book:
    """
    Add info about book into the review system
    Args:
        db: database session object
        book: Book object with data to be saved

    Returns:
        the instance of the book, throws error if the given values a duplicate
    """
    _book = db.query(Book).filter(and_(
        Book.title == book.title,
        Book.author_name == book.author_name,
        Book.publication_year == book.publication_year,
    )).first()
    if _book is not None:
        raise ValueError(ErrorCodes.BOOK_ALREADY_EXISTS.message)

    new_book = Book(title=book.title,
                    author_name=book.author_name,
                    publication_year=book.publication_year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
