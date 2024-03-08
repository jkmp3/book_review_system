"""Contains schemas used for response objects"""
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """
    Represents an error response, returned during unexpected scenarios

    code (int): error
    message (string): descriptive error message
    """
    code: int
    message: str
