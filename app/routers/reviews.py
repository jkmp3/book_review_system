from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.enums.codes import ApplicationCodes
from app.repositories import review_repository
from app.schemas.request_schemas import ReviewSchema
from app.schemas.response_schemas import OkayResponse
from app.utils.db_utils import get_db_session

router = APIRouter()


@router.post("/books/reviews")
def add_review(review: ReviewSchema, db: Session = Depends(get_db_session)):
    review = review_repository.add_review(db, review)
    return OkayResponse(code=ApplicationCodes.OKAY, result=review).dict()


@router.get("/books/reviews")
def get_reviews(db: Session = Depends(get_db_session)):
    reviews = review_repository.get_reviews(db)
    return {"reviews": reviews}
