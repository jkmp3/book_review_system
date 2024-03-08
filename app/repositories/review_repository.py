"""Database operations related to review entity"""
from typing import Type, Optional

from sqlalchemy.orm import Session

from app.models.models import Review
from app.schemas.request_schemas import ReviewSchema


def get_reviews(db: Session) -> list[Type[Review]]:
    """
    Get the reviews of books
    Args:
        db: database session object

    Returns:
        List of the reviews in the review system
    """
    return db.query(Review).all()


def add_review(db: Session, review: ReviewSchema) -> Optional[Review]:
    """
    Adds a review into the system
    Args:
        db: database session object
        review: review instance with data to be saved

    Returns:
        the review instance that was saved
    """
    new_review = Review(review_text=review.review_text,
                        rating=review.rating,
                        book_id=review.book_id)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review
