from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


class YearRequest(BaseModel):
    year: int = Field(ge=2000, le=2100)


class DateRequest(BaseModel):
    date: date


class Holiday(BaseModel):
    name: str = Field(min_length=2)
    date: date
    type: str = "national"

    date_basis: Literal["fixed", "movable"] = "fixed"

    status: Literal["confirmed", "estimated"] = "estimated"


class HolidayDataset(BaseModel):
    year: int = Field(ge=2000, le=2100)

    country: str = "Nigeria"

    status: Literal["partial", "complete"]

    holidays: list[Holiday] = Field(min_length=1)

    source: str = Field(min_length=3)

    last_updated: date