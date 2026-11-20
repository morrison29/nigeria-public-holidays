import json
from pathlib import Path

from datetime import date

from app.models import HolidayDataset


DATA_DIR = Path(__file__).parent / "data"


def load_dataset(year: int):
    """
    Load and validate a holiday dataset for a given year.
    """

    data_file = DATA_DIR / f"holidays_{year}.json"

    if not data_file.exists():
        return None

    with open(data_file, "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    # Validate JSON data against the Pydantic model
    dataset = HolidayDataset.model_validate(raw_data)

        # Ensure every holiday belongs to the dataset year
    for holiday in dataset.holidays:
        if holiday.date.year != year:
            raise ValueError(
                f"{holiday.name} has a date outside dataset year {year}"
            )

    # Prevent duplicate holiday dates
    dates = [holiday.date for holiday in dataset.holidays]

    if len(dates) != len(set(dates)):
        raise ValueError("Duplicate holiday dates found in dataset")

    # Prevent duplicate holiday names
    names = [holiday.name.lower() for holiday in dataset.holidays]

    if len(names) != len(set(names)):
        raise ValueError("Duplicate holiday names found in dataset")

    # Ensure the dataset matches the requested year
    if dataset.year != year:
        raise ValueError(
            f"Dataset year mismatch: expected {year}, got {dataset.year}"
        )

    return dataset


def get_holiday_dataset(year: int):
    return load_dataset(year)


def get_holidays(year: int):
    dataset = load_dataset(year)

    if dataset is None:
        return None

    return dataset.holidays


def check_holiday(target_date: date):
    holidays = get_holidays(target_date.year)

    if holidays is None:
        return None

    for holiday in holidays:
        if holiday.date == target_date:
            return holiday.model_dump(mode="json")

    return None


def is_working_day(target_date: date):
    holidays = get_holidays(target_date.year)

    if holidays is None:
        return None

    if target_date.weekday() >= 5:
        return False

    return check_holiday(target_date) is None