from functions.level_1.five_title import change_copy_item


def test__change_copy_item__should_return_title_with_prefix_copy_of():
    assert change_copy_item("Test title") == "Copy of Test title"

def test__change_copy_item__should_return_title_with_number_of_copy():
    assert change_copy_item("Copy of Test title") == "Copy of Test title (2)"

def test__change_copy_item__should_increment_number_of_copy():
    assert change_copy_item("Copy of Test title (2)") == "Copy of Test title (3)"

def test__change_copy_item__should_create_number_of_copy_and_ignore_parentheses():
    assert change_copy_item("Copy of Test title (a)") == "Copy of Test title (a) (2)"
