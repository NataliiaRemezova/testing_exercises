import datetime
from functions.level_1.two_date_parser import compose_datetime_from

def test_compose_datetime_from_tomorrow():
    expected_date = datetime.date.today() + datetime.timedelta(days=1)
    expected_datetime = datetime.datetime(expected_date.year, expected_date.month, expected_date.day, 10, 00)
    assert compose_datetime_from("tomorrow", "10:00") == expected_datetime

def test_compose_datetime_from_today():
    expected_date = datetime.date.today()
    expected_datetime = datetime.datetime(expected_date.year, expected_date.month, expected_date.day, 8, 00)
    assert compose_datetime_from("", "8:00") == expected_datetime