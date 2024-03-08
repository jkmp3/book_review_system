from sqlalchemy.orm import Session

from app.models.models import Review
from app.schemas.schemas import ReviewSchema


def get_reviews(db: Session):
    return db.query(Review).all()


def add_review(db: Session, review: ReviewSchema):
    new_review = Review(review_text=review.review_text,
                        rating=review.rating,
                        book_id=review.book_id)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review
