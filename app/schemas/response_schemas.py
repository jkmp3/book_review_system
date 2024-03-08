"""Contains schemas used for response objects"""
from pydantic import BaseModel


class Response(BaseModel):
    """
    Represents a regular response object

    code (int): error code
    """

    code: int


class OkayResponse(Response):
    """
    Represents a regular response object

    code (int): error code
    result (object): result of the API call
    """

    code: int
    result: object


class PaginatedResponse(OkayResponse):
    """
    Represents a regular response object

    code (int): error code
    result (object): result of the API call
    """

    limit: int
    offset: int


class BadRequestResponse(Response):
    """
    Represents an error response, returned during unexpected scenarios

    code (int): error
    message (string): descriptive error message
    """
    message: str
