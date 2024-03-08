from typing import Optional

from sqlalchemy.orm import Session

from app.enums.string_comparison import StringComparison
from app.models.models import Book
from app.schemas.schemas import BookSchema, TextFilterSchema, RangeFilterSchema


def get_books(db: Session,
              text_filter: Optional[TextFilterSchema] = None,
              range_filter: Optional[RangeFilterSchema] = None):
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


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def add_book(db: Session, book: BookSchema):
    new_book = Book(title=book.title,
                    author_name=book.author_name,
                    publication_year=book.publication_year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
