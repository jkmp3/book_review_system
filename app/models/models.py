"""Contains ORM equivalent classes to the tables stored in database"""


from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.config.config import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    author_name = Column(String)
    publication_year = Column(Integer)


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review_text = Column(String)
    rating = Column(Float)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
