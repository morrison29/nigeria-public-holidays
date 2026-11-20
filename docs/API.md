# Nigeria Public Holidays API — API Reference

## Base URL

Local development:

```text
http://localhost:8000
```

Production URL will be added after public deployment.

## Authentication

The current development version does not require authentication.

## Content Type

All POST requests use:

```text
Content-Type: application/json
```

## 1. Health Check

**GET `/health`**

Checks whether the API service is operational.

Example response:

```json
{
  "status": "healthy",
  "service": "Nigeria Public Holidays API"
}
```

## 2. Retrieve Holidays

**POST `/v1/holidays`**

Retrieves the holiday dataset for a specified year.

Request:

```json
{
  "year": 2027
}
```

Successful response:

```json
{
  "country": "Nigeria",
  "year": 2027,
  "dataset_available": true,
  "dataset_status": "partial",
  "source": "Calendar calculations; official announcements pending",
  "last_updated": "2026-11-20",
  "holidays": []
}
```

The holidays array contains the available holiday records.

If the requested year is unavailable:

```json
{
  "country": "Nigeria",
  "year": 2028,
  "dataset_available": false,
  "message": "Holiday dataset is not available for this year."
}
```

## 3. Check a Public Holiday

**POST `/v1/check-date`**

Checks whether a date is listed as a public holiday.

Request:

```json
{
  "date": "2027-01-01"
}
```

Response:

```json
{
  "date": "2027-01-01",
  "dataset_available": true,
  "dataset_status": "partial",
  "is_public_holiday": true,
  "holiday": {
    "name": "New Year's Day",
    "date": "2027-01-01",
    "type": "national",
    "date_basis": "fixed",
    "status": "estimated"
  }
}
```

## 4. Check a Working Day

**POST `/v1/working-day`**

Determines whether a date is a working day.

Request:

```json
{
  "date": "2027-01-04"
}
```

Example response:

```json
{
  "date": "2027-01-04",
  "dataset_available": true,
  "dataset_status": "partial",
  "is_working_day": true
}
```

The calculation considers weekends and holidays listed in the available dataset.

## Data Fields

| Field | Description |
|---|---|
| country | Country covered by the dataset |
| year | Calendar year |
| dataset_available | Whether the requested dataset exists |
| dataset_status | Whether the dataset is partial or complete |
| source | Dataset source description |
| last_updated | Date the dataset was last updated |
| name | Holiday name |
| date | Holiday date |
| type | Holiday classification |
| date_basis | Fixed or movable date |
| status | Confirmed or estimated |

## HTTP Status Codes

| Code | Meaning |
|---|---|
| 200 | Request successful |
| 422 | Invalid request |
| 500 | Internal server or dataset validation error |

## Important Notes

- A partial dataset does not represent every holiday in that year.
- Estimated dates must not be interpreted as official government announcements.
- Islamic holiday dates may change following official announcements.
- An unavailable dataset does not mean that no public holidays exist for that year.

## Interactive Documentation

FastAPI Swagger documentation:

```text
/docs
```

Alternative documentation:

```text
/redoc
```