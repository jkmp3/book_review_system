from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

from app.enums.string_comparison import StringComparison


class BookSchema(BaseModel):
    title: str = Field(min_length=1, max_length=256)
    author_name: str = Field(min_length=1, max_length=256)
    publication_year: int = Field(le=datetime.now().year)


class FieldFilterSchema(BaseModel):
    field: str


class TextFilterSchema(FieldFilterSchema):
    text: str
    operation: StringComparison = StringComparison.EQUALS_IGNORE_CASE


class RangeFilterSchema(FieldFilterSchema):
    lower_bound: int = 0
    upper_bound: int = Field(gt=lower_bound)


class FilterSchema(BaseModel):
    text_filter: Optional[TextFilterSchema] = None
    range_filter: Optional[RangeFilterSchema] = None


class ReviewSchema(BaseModel):
    review_text: str = Field(min_length=1, max_length=1024)
    rating: Decimal = Field(ge=1, le=5, decimal_places=2)
    book_id: int = Field()
