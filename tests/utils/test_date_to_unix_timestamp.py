from investment_analysis.utils.parse_to_timestamp import (
    parse_to_unix_timestamp,
)


def test_date_to_unix_timestamp() -> None:
    assert parse_to_unix_timestamp("Monday, January 01, 2021") == 1609455600000
    assert (
        parse_to_unix_timestamp("Tuesday, February 02, 2021") == 1612220400000
    )
    assert parse_to_unix_timestamp("Wednesday, March 03, 2021") == 1614726000000


def test_date_to_unix_timestamp_with_different_format() -> None:
    assert parse_to_unix_timestamp("01/01/2021", "%m/%d/%Y") == 1609455600000
    assert parse_to_unix_timestamp("02-02-2021", "%m-%d-%Y") == 1612220400000
    assert parse_to_unix_timestamp("2021.03.03", "%Y.%m.%d") == 1614726000000
