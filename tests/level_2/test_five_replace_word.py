import pytest
from functions.level_2.five_replace_word import replace_word

@pytest.mark.parametrize(
    "test_text, replace_from, replace_to, expected_result",
    [
        ("This is a test text", "text", "example", "This is a test example"),
        ("This is a test Text", "text", "example", "This is a test example"),
    ]
)
def test__replace_word__should_replace_string_and_handle_capitalization(test_text, replace_from, replace_to, expected_result):
    assert replace_word(text=test_text, replace_from=replace_from, replace_to=replace_to) == expected_result

def test__replace_word__should_not_replace_with_incorrect_capitalization():
    test_text = "This is a test Text"
    assert replace_word(text = test_text, replace_from = "text", replace_to = "Example") != "This is a test example"