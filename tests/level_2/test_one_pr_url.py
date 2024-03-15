from functions.level_2.one_pr_url import is_github_pull_request_url
import pytest

@pytest.mark.parametrize(
        "url",
        [
            ("https://github.com/JohnDoe/testing_exercises/pull/1"),
            ("https://github.com/JohnDoe/testing_exercises/pull/55d3fo")
        ]
)
def test__is_github_pull_request_url__should_check_correct_url(url: str):
    assert is_github_pull_request_url(url) is True

@pytest.mark.parametrize(
        "url",
        [
            ("https://test.com/JohnDoe/testing_exercises/pull/1"),
            ("https://github.com.com/JohnDoe/testing_exercises/pull/55d3fo")
        ]
)
def test__is_github_pull_request_url__should_check_not_github_url(url: str):
    assert is_github_pull_request_url(url) is False

@pytest.mark.parametrize(
        "url",
        [
            ("https://github.com/JohnDoe/testing_exercises/pulllll/1"),
            ("https://github.com/JohnDoe/testing_exercises/55d3fo")
        ]
)
def test__is_github_pull_request_url__should_check_not_pr_url(url: str):
    assert is_github_pull_request_url(url) is False