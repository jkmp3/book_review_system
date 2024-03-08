"""Custom error codes and messages with both error code and message."""

import enum


@enum.unique
class ApplicationCodes(enum.IntEnum):
    """
    Custom codes used in application
    """
    OKAY = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404


class ErrorCodes(enum.Enum):
    """
    Custom error class with both error ID and message.
    """
    BOOK_ALREADY_EXISTS = (ApplicationCodes.BAD_REQUEST,
                           "Book already exists, try again with different values")
    BOOK_DOES_NOT_EXIST = (ApplicationCodes.NOT_FOUND,
                           "Book does not exist, try again with different id")

    def __init__(self, error_id: int, message: str):
        self.error_id = error_id
        self.message = message
