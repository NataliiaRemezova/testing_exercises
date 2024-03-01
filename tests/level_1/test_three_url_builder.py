from functions.level_1.three_url_builder import build_url


def test_build_url_no_params():
    assert build_url("test.com", "test") == "test.com/test"

def test_build_url_single_param():
    assert build_url("test.com", "test", {"a": "1"}) == "test.com/test?a=1"


def test_build_url_two_params():
    assert build_url("test.com", "test", {"a": "1", "b": "2"}) == "test.com/test?a=1&b=2"

def test_build_url_no_relative_url():
    assert build_url("test.com", "") == "test.com/"


