# Nigeria Public Holidays API

A RESTful API providing structured information about Nigerian public holidays, date verification and working-day calculations.

Built with Python and FastAPI, the service is designed to help developers integrate Nigerian public holiday information into applications, business systems and scheduling tools.

## Features

- Retrieve Nigerian public holidays by year.
- Check whether a particular date is a public holiday.
- Determine whether a date is a working day.
- Support multiple yearly holiday datasets.
- Distinguish between complete and partial datasets.
- Identify estimated and confirmed holiday dates.
- Validate holiday records using Pydantic.
- Docker-based deployment.
- Automated API testing.

## Technology Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- HTTPX
- Docker

## Project Structure

```text
nigeria-public-holidays/
│
├── app/
│   ├── data/
│   │   ├── holidays_2026.json
│   │   └── holidays_2027.json
│   │
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── holidays.py
│
├── tests/
│   └── test_api.py
│
├── docs/
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd nigeria-public-holidays
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

Alternative documentation:

```text
http://localhost:8000/redoc
```

## API Endpoints

### 1. Health Check

**GET `/health`**

Checks whether the API is running.

Example response:

```json
{
  "status": "healthy",
  "service": "Nigeria Public Holidays API"
}
```

### 2. Retrieve Public Holidays

**POST `/v1/holidays`**

Retrieves the available holiday dataset for a requested year.

Request:

```json
{
  "year": 2027
}
```

The response includes:

- Country
- Year
- Dataset availability
- Dataset status
- Data source
- Last updated date
- Holiday records

### 3. Check a Public Holiday

**POST `/v1/check-date`**

Checks whether a particular date is listed as a public holiday.

Request:

```json
{
  "date": "2027-01-01"
}
```

The response indicates whether the date is a public holiday and returns the matching holiday record when available.

### 4. Check a Working Day

**POST `/v1/working-day`**

Determines whether a date is a working day.

Request:

```json
{
  "date": "2027-01-04"
}
```

The API considers weekends and listed public holidays when calculating working days.

## Dataset Coverage

The project currently includes datasets for:

| Year | Availability |
|---|---|
| 2026 | Partial |
| 2027 | Partial |

A partial dataset means that the available records should not be interpreted as a complete official holiday calendar.

Holiday records distinguish between:

- `confirmed`: Supported by an official announcement.
- `estimated`: Based on a calendar calculation or prediction.
- `fixed`: Falls on a predetermined calendar date.
- `movable`: Its calendar date changes between years.

Islamic holiday dates may be subject to moon sighting and official government announcements.

The API should not be treated as an authoritative source for unconfirmed holiday dates.

## Adding a New Year

Create a new JSON file inside:

```text
app/data/
```

Use this naming convention:

```text
holidays_2028.json
```

Follow the existing dataset structure:

```json
{
  "year": 2028,
  "country": "Nigeria",
  "status": "partial",
  "source": "Source description",
  "last_updated": "2027-01-01",
  "holidays": [
    {
      "name": "New Year's Day",
      "date": "2028-01-01",
      "type": "national",
      "date_basis": "fixed",
      "status": "estimated"
    }
  ]
}
```

The application automatically loads datasets based on the requested year.

Ensure that all records are accurate and appropriately classified before adding them.

## Running Tests

Run the automated test suite:

```bash
python -m pytest -v
```

The current test suite covers:

- API health checks.
- Holiday retrieval.
- Multiple yearly datasets.
- Unavailable years.
- Public holiday verification.
- Working-day calculations.
- Weekend detection.
- Invalid request validation.
- Dataset error handling.

## Docker Deployment

Build the Docker image:

```bash
docker build -t nigeria-public-holidays .
```

Run the container:

```bash
docker run -d -p 8000:8000 --name nigeria-holidays-api nigeria-public-holidays
```

Check the running container:

```bash
docker ps
```

View application logs:

```bash
docker logs nigeria-holidays-api
```

Stop the container:

```bash
docker stop nigeria-holidays-api
```

## Data Sources and Accuracy

Holiday information should be maintained using reliable sources, particularly official Nigerian government announcements.

Relevant sources include:

- Federal Ministry of Interior.
- Federal Government announcements.
- Relevant religious calendar calculations for estimated movable holidays.

Every dataset should identify its source and last-updated date.

Official announcements should take precedence over estimates.

## Error Handling

The API provides structured responses for unavailable datasets and invalid requests.

Common HTTP status codes include:

| Status | Meaning |
|---|---|
| 200 | Request successful |
| 422 | Invalid request data |
| 500 | Internal server or dataset validation error |

## Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Run the automated tests.
5. Submit a pull request with a clear description.

Please ensure holiday dates are properly sourced and classified.

## Project Status

The project is under active development.

Docker containerisation and automated testing have been completed locally.

Public hosting, Pocket service integration and end-to-end Pocket request verification are still pending.

## Licence

A licence will be added before public release.