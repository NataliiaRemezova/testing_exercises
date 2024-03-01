from functions.level_2.one_pr_url import is_github_pull_request_url

def test__is_github_pull_request_url__url_correct():
    url = "https://github.com/JohnDoe/testing_exercises/pull/1"
    assert is_github_pull_request_url(url) == True

def test__is_github_pull_request_url__url_not_github():
    url = "https://test.com/JohnDoe/testing_exercises/pull/1"
    assert is_github_pull_request_url(url) == False

def test__is_github_pull_request_url__url_not_pr():
    url = "https://github.com/JohnDoe"
    assert is_github_pull_request_url(url) == False