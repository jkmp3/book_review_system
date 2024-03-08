"""Contains enums for supported string operations"""

import enum


class StringComparison(str, enum.Enum):
    """
    StringComparison defines the available comparison operators for
    string-based filtering in queries.

    Members:
        EQUALS (str): Performs a case-sensitive exact match.
        EQUALS_IGNORE_CASE (str): Performs a case-insensitive exact match.
        CONTAINS (str): Performs a substring search.
        CONTAINS_IGNORE_CASE (str): Performs a case-insensitive substring search.
    """
    EQUALS = "equals"
    EQUALS_IGNORE_CASE = "equals_ignore_case"
    CONTAINS = "contains"
    CONTAINS_IGNORE_CASE = "contains_ignore_case"
