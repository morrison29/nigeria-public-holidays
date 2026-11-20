from datetime import date

from fastapi import FastAPI, HTTPException
import logging
from app.models import YearRequest, DateRequest
from app.holidays import (
    get_holiday_dataset,
    check_holiday,
    is_working_day
)


app = FastAPI(
    title="Nigeria Public Holidays API",
    description=(
        "An API providing Nigerian public holiday information, "
        "holiday date checks and working-day calculations."
    ),
    version="1.0.0"
)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safely_load_dataset(year: int):
    try:
        return get_holiday_dataset(year)

    except (ValueError, KeyError) as error:
        logger.error(
            "Invalid holiday dataset for %s: %s",
            year,
            error
        )

        raise HTTPException(
            status_code=500,
            detail="Holiday dataset is currently unavailable due to a data validation error."
        )

    except Exception:
        logger.exception(
            "Unexpected error loading holiday dataset for %s",
            year
        )

        raise HTTPException(
            status_code=500,
            detail="An unexpected server error occurred."
        )

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Nigeria Public Holidays API"
    }


@app.post("/v1/holidays")
def list_holidays(request: YearRequest):

    dataset = safely_load_dataset(request.year)

    if dataset is None:
        return {
            "country": "Nigeria",
            "year": request.year,
            "dataset_available": False,
            "message": "Holiday dataset is not available for this year."
        }

    return {
        "country": dataset.country,
        "year": dataset.year,
        "dataset_available": True,
        "dataset_status": dataset.status,
        "source": dataset.source,
        "last_updated": dataset.last_updated,
        "holidays": [h.model_dump(mode="json") for h in dataset.holidays]
    }


@app.post("/v1/check-date")
def check_date(request: DateRequest):

    dataset = safely_load_dataset(request.date.year)

    if dataset is None:
        return {
            "date": request.date,
            "dataset_available": False,
            "is_public_holiday": None,
            "holiday": None,
            "message": "Holiday dataset is not available for this year."
        }

    holiday = check_holiday(request.date)

    return {
        "date": request.date,
        "dataset_available": True,
        "dataset_status": dataset.status,
        "is_public_holiday": holiday is not None,
        "holiday": holiday
    }


@app.post("/v1/working-day")
def check_working_day(request: DateRequest):

    dataset = safely_load_dataset(request.date.year)

    if dataset is None:
        return {
            "date": request.date,
            "dataset_available": False,
            "is_working_day": None,
            "message": "Holiday dataset is not available for this year."
        }

    result = is_working_day(request.date)

    return {
        "date": request.date,
        "dataset_available": True,
        "dataset_status": dataset.status,
        "is_working_day": result
    }