from functions.level_2.one_pr_url import is_github_pull_request_url

def test__is_github_pull_request_url__should_check_correct_url():
    url = "https://github.com/JohnDoe/testing_exercises/pull/1"
    assert is_github_pull_request_url(url) == True

def test__is_github_pull_request_url__should_check_not_github_url():
    url = "https://test.com/JohnDoe/testing_exercises/pull/1"
    assert is_github_pull_request_url(url) == False

def test__is_github_pull_request_url__should_check_not_pr_url():
    url = "https://github.com/JohnDoe"
    assert is_github_pull_request_url(url) == False