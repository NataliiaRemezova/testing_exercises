import datetime
import pytest
from functions.level_1.two_date_parser import compose_datetime_from

@pytest.mark.parametrize("time", [("10:00"), ("23:59"), ("13:00")])
def test__compose_datetime_from__should_return_tomorrows_datetime_if_input_is_tomorrow(time: str):
    assert compose_datetime_from("tomorrow", time).date() == (datetime.date.today() + datetime.timedelta(days=1))

@pytest.mark.parametrize("datestr", ["today", "unknown", ""])
def test__compose_datetime_from__should_return_todays_datetime_if_input_is_not_tomorrow(datestr: str):
    assert compose_datetime_from(datestr, "10:00").date() == datetime.date.today()

@pytest.mark.parametrize(
        "time,hour,minute",
        [
            ("10:00", 10, 0),
            ("23:59", 23, 59),
            ("13:00", 13, 0)
        ]
)
def test__compose_datetime_from__should_return_todays_datetime_with_correct_time(
    time: str, hour: int, minute: int):
    today = datetime.date.today()
    assert compose_datetime_from("today", time).time() == datetime.time(hour, minute)
    