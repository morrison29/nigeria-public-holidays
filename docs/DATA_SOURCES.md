# Nigeria Public Holidays API — Data Sources and Verification Policy

## 1. Purpose

This document establishes how holiday information is collected, classified, verified and maintained within the Nigeria Public Holidays API.

The objective is to ensure that developers and users can distinguish between officially confirmed holidays and estimated calendar dates.

## 2. Preferred Data Sources

The project prioritises the following sources:

### Federal Ministry of Interior

Primary reference for official Nigerian public holiday declarations.

Website: https://interior.gov.ng/

### Federal Government Announcements

Official announcements concerning public holidays, including special declarations and changes to previously announced dates.

### Established Calendar References

Reliable calendar references may be used to calculate dates for movable holidays, including Easter-related dates and Islamic observances.

Calendar calculations must not be presented as official government confirmation.

## 3. Holiday Classification

Every holiday record must contain the following fields:

| Field | Description |
|---|---|
| name | Holiday name |
| date | Calendar date |
| type | Holiday classification |
| date_basis | Fixed or movable |
| status | Confirmed or estimated |

### Date Basis

**Fixed:** The holiday follows a predetermined calendar date.

**Movable:** The holiday date changes between calendar years.

### Confirmation Status

**Confirmed:** Supported by an official government announcement.

**Estimated:** Calculated or predicted but not yet officially confirmed.

## 4. Dataset Status

Each yearly dataset has a status.

**Partial:** Some holiday records are available, but the dataset has not been verified as complete.

**Complete:** The year's holiday coverage has been reviewed against the applicable official announcements and relevant calendar information.

A dataset must not be marked complete simply because it contains the expected fixed holidays.

## 5. Verification Procedure

Before adding a holiday:

1. Identify the holiday.
2. Locate a reliable source.
3. Verify the date.
4. Determine whether the date is fixed or movable.
5. Determine whether it is officially confirmed or estimated.
6. Add the record to the appropriate yearly dataset.
7. Run the automated tests.
8. Record the dataset update date.

## 6. Handling Changes

If the Nigerian government announces a different date:

1. Review the official announcement.
2. Update the affected holiday record.
3. Change its status where appropriate.
4. Update the dataset's last_updated field.
5. Run the automated tests.
6. Document the change.

Historical dataset changes should be traceable through Git commits.

## 7. Data Accuracy Limitations

The API provides structured holiday information based on the datasets maintained in the project.

It does not independently guarantee that every listed date has been officially declared.

In particular:

- Islamic holiday dates may depend on moon sighting.
- Special public holidays may be announced by the government.
- Estimated dates may change.
- Partial datasets may omit holidays.

Developers should check official announcements before using unconfirmed dates for critical scheduling decisions.

## 8. Dataset Maintenance

Each dataset is stored separately:

```text
app/data/
├── holidays_2026.json
└── holidays_2027.json
```

Future datasets should follow the same naming convention:

```text
holidays_2028.json
holidays_2029.json
```

All datasets must pass Pydantic validation before being served by the API.

## 9. Update History

Record significant dataset changes here.

| Date | Year | Description |
|---|---|---|
| 2026-11-20 | 2026 | Initial dataset structure |
| 2026-11-20 | 2027 | Initial partial dataset |

Update this table whenever significant changes are made.