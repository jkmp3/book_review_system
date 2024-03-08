"""Contains enums for supported string operations"""

import enum


class StringComparison(str, enum.Enum):
    EQUALS = "equals"
    EQUALS_IGNORE_CASE = "equals_ignore_case"
    CONTAINS = "contains"
    CONTAINS_IGNORE_CASE = "contains_ignore_case"
