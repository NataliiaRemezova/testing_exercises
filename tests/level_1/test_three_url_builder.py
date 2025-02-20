from functions.level_1.three_url_builder import build_url
import pytest

@pytest.mark.parametrize(
        "host_name,relative_url",
        [
            ("test.com", "test"),
            ("test-te.st.com", "best")
        ]
)
def test__build_url__should_return_url_with_no_params(host_name: str, relative_url: str):
    assert build_url(host_name, relative_url) == f'{host_name}/{relative_url}'

@pytest.mark.parametrize(
        "host_name,relative_url,get_params",
        [
            ("test.com", "test", {"a": "1"}),
            ("test-te.st.com", "best", {"b": "5"})
        ]
)
def test__build_url__should_return_url_with_single_param(host_name: str, relative_url: str, get_params: dict):
    assert build_url(host_name, relative_url, get_params) == f'{host_name}/{relative_url}?{list(get_params.keys())[0]}={list(get_params.values())[0]}'

@pytest.mark.parametrize(
        "host_name,relative_url,get_params",
        [
            ("test.com", "test", {"a": "1", "b": "2"}),
            ("test-te.st.com", "best", {"b": "13", "bccc": "22"})
        ]
)
def test__build_url__should_return_url_with_two_params(host_name: str, relative_url: str, get_params: dict):
    assert build_url(host_name, relative_url, get_params) == (f'{host_name}/{relative_url}?'
    f'{list(get_params.keys())[0]}={list(get_params.values())[0]}&'
    f'{list(get_params.keys())[1]}={list(get_params.values())[1]}')

@pytest.mark.parametrize(
        "host_name,relative_url",
        [
            ("test.com", ""),
            ("test-te.st.com", "")
        ]
)
def test__build_url__should_return_url_with_no_relative_url(host_name: str, relative_url: str):
    assert build_url(host_name, relative_url) ==  f'{host_name}/{relative_url}'
