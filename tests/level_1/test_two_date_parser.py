import datetime
import pytest
from functions.level_1.two_date_parser import compose_datetime_from

@pytest.mark.parametrize(
        "date,time",
        [
            ("tomorrow", "10:00"),
            ("tomorrow", "23:59"),
            ("tomorrow", "13:00")
        ]
)
def test__compose_datetime_from__should_return_tomorrows_datetime_if_input_is_tomorrow(date: str, time: str):
    assert compose_datetime_from(date, time).date() == (datetime.date.today() + datetime.timedelta(days=1))

@pytest.mark.parametrize(
        "date,time",
        [
            ("today", "10:00"),
            ("unknown", "23:59"),
            ("", "13:00")
        ]
)
def test__compose_datetime_from__should_return_todays_datetime_if_input_is_not_tomorrow(date: str, time: str):
    assert compose_datetime_from(date, time).date() == datetime.date.today()

@pytest.mark.parametrize(
        "date,time,expected_hour,expected_minutes",
        [
            ("today", "10:00", 10, 0),
            ("unknown", "23:59", 23, 59),
            ("", "13:00", 13, 0)
        ]
)
def test__compose_datetime_from__should_return_todays_datetime_with_correct_time(
    date: str, time: str, expected_hour: int, expected_minutes: int):
    today = datetime.date.today()
    assert compose_datetime_from(date, time).time() == datetime.time(hour=expected_hour, minute=expected_minutes)
    