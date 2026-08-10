from datetime import date
from seasons import calculate_minutes


def test_one_year():
    assert calculate_minutes(date(2024, 1, 1), date(2025, 1, 1)) == 527040


def test_two_years():
    assert calculate_minutes(date(2023, 1, 1), date(2025, 1, 1)) == 1052640


def test_same_day():
    assert calculate_minutes(date(2025, 1, 1), date(2025, 1, 1)) == 0


def test_leap_year():
    assert calculate_minutes(date(2020, 1, 1), date(2021, 1, 1)) == 527040
