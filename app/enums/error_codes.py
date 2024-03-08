"""Custom error codes and messages with both error code and message."""

import enum


class ErrorCodes(enum.Enum):
    """
    Custom error class with both error ID and message.
    """
    BOOK_ALREADY_EXISTS = (101, "Book already exists, try again with different values")
    BOOK_DOES_NOT_EXIST = (102, "Book does not exist, try again with different id")

    def __init__(self, error_id: int, message: str):
        self.error_id = error_id
        self.message = message
