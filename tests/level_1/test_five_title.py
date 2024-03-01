from functions.level_1.five_title import change_copy_item


def test_change_copy_item_prefix():
    assert change_copy_item("Test title") == "Copy of Test title"

def test_change_copy_item_with_number():
    assert change_copy_item("Copy of Test title") == "Copy of Test title (2)"

def test_change_copy_item_increment_number():
    assert change_copy_item("Copy of Test title (2)") == "Copy of Test title (3)"

def test_change_copy_item_parentheses():
    assert change_copy_item("Copy of Test title (a)") == "Copy of Test title (a) (2)"
