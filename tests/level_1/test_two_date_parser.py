import datetime
from functions.level_1.two_date_parser import compose_datetime_from

def test__compose_datetime_from__should_return_tomorrows_datetime_if_input_is_tomorrow():
    assert compose_datetime_from("tomorrow", "10:00").day == (datetime.date.today() + datetime.timedelta(days=1)).day

def test__compose_datetime_from__should_return_todays_datetime_if_input_is_not_tomorrow():
    assert compose_datetime_from("", "8:00").day == datetime.date.today().day

def test__compose_datetime_from__should_return_todays_datetime_with_correct_time():
    today = datetime.date.today()
    today_datetime = datetime.datetime(today.year, today.month, today.day, 8, 00)
    assert compose_datetime_from("", "8:00") == today_datetime