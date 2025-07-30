"""User-related Pydantic schemas for API input/output serialization."""

# -- Imports


import json
from enum import IntEnum, Enum
from typing import Type, List
from pydantic import BaseModel, Field
from sqlalchemy.types import TypeDecorator, TEXT


# --


class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"


class AgeEnum(IntEnum):
    pass


AgeEnum = IntEnum("AgeEnum", {f"AGE_{i}": i for i in range(14, 100)})


class Zodiacs(str, Enum):
    ARIES = "Aries"
    TAURUS = "Taurus"
    GEMINI = "Gemini"
    CANCER = "Cancer"
    LEO = "Leo"
    VIRGO = "Virgo"
    LIBRA = "Libra"
    SCORPIO = "Scorpio"
    SAGITTARIUS = "Sagittarius"
    CAPRICORN = "Capricorn"
    AQUARIUS = "Aquarius"
    PISCES = "Pisces"


class PydanticJsonType(TypeDecorator):
    """SQLAlchemy column type for storing Pydantic models as JSON."""

    impl = TEXT
    cache_ok = True

    def __init__(self, model: Type[BaseModel], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    def process_bind_param(self, value):
        if value is not None:
            return value.json()
        return None

    def process_result_value(self, value):
        if value is not None:
            return self.model.model_validate_json(value)
        return None


class UserDescription(BaseModel):
    hobbies: List[str]
    profession: str
    bio: str
    goals: str
    preferences: str


class UserBaseData(BaseModel):
    name: str
    age: AgeEnum = AgeEnum.AGE_18
    height: int | None = None
    weight: int | None = None
    gender: Gender
    zodiac: Zodiacs
