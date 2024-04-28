from enum import Enum


class CaseInsensitiveStrEnum(str, Enum):

    @classmethod
    def _missing_(cls, value: object) -> "CaseInsensitiveStrEnum":
        # Allow case-insensitive access to the enum values
        if not isinstance(value, str):
            raise TypeError(f"{cls.__name__} members must be of type str")

        for member in cls:
            if member.lower() == value.lower():
                return member
        raise ValueError(f"{cls.__name__} does not have a member named {value}")
