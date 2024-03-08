from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.repositories import review_repository
from app.schemas.schemas import ReviewSchema
from app.utils.db_utils import get_db_session

router = APIRouter()


@router.post("/books/reviews")
async def add_review(review: ReviewSchema, db: Session = Depends(get_db_session)):
    review_repository.add_review(db, review)
    return {"message": "Review added successfully."}


@router.get("/books/reviews")
async def get_reviews(db: Session = Depends(get_db_session)):
    reviews = review_repository.get_reviews(db)
    return {"reviews": reviews}
