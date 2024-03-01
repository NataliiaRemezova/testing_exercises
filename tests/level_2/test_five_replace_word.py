from functions.level_2.five_replace_word import replace_word


def test__replace_word__replace_lowercase_string():
    test_text = "This is a test text"
    assert replace_word(text = test_text, replace_from = "text", replace_to = "example") == "This is a test example"

def test__replace_word__replace_capitalized_string_with_lowercase_replace_from():
    test_text = "This is a test Text"
    assert replace_word(text = test_text, replace_from = "text", replace_to = "example") == "This is a test example"

def test__replace_word__replace_with_capitalized_replace_to():
    test_text = "This is a test Text"
    assert replace_word(text = test_text, replace_from = "text", replace_to = "Example") != "This is a test example"