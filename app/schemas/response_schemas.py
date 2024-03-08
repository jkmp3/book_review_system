"""Contains schemas used for response objects"""
from pydantic import BaseModel


class Response(BaseModel):
    """
    Represents a regular response object

    code (int): code, 200 for success
    """

    code: int = 200


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

    limit (int): number of items per "page"
    offset (int): results start from this index (index starts from 0)
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
