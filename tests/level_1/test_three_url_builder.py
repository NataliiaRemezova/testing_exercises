from functions.level_1.three_url_builder import build_url


def test__build_url__should_return_url_with_no_params():
    assert build_url("test.com", "test") == "test.com/test"

def test__build_url__should_return_url_with_single_param():
    assert build_url("test.com", "test", {"a": "1"}) == "test.com/test?a=1"


def test__build_url__should_return_url_with_two_params():
    assert build_url("test.com", "test", {"a": "1", "b": "2"}) == "test.com/test?a=1&b=2"

def test__build_url__should_return_url_with_no_relative_url():
    assert build_url("test.com", "") == "test.com/"


