"""Contains ORM equivalent classes to the tables stored in database"""


from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.config.config import Base


class Book(Base):
    """
    Represents a book in the book review system.

    Attributes:
        id (int): Unique identifier for the book
        title (str): The title of the book.
        author_name (str): The name of the author.
        publication_year (int): The year the book was published.
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    author_name = Column(String)
    publication_year = Column(Integer)


class Review(Base):
    """
    Represents an anonymous review about a book in the review system.

    Attributes:
        id (int): Unique identifier for the review
        review_text (str): Review about the book
        rating (float): Decimal rating out of 5.
        book_id (int): The id of the book.
    """
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review_text = Column(String)
    rating = Column(Float)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
