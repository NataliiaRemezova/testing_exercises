from functions.level_1.five_title import change_copy_item
import pytest

@pytest.mark.parametrize(
        "title",
        [
            ("Test title"),
            ("Tes3t 2tit.le")
        ]
)
def test__change_copy_item__should_return_title_with_prefix_copy_of(title: str):
    assert change_copy_item(title) == f'Copy of {title}'

@pytest.mark.parametrize(
        "title",
        [
            ("Copy of Test title"),
            ("Copy of T3.est 3..2titl3e")
        ]
)
def test__change_copy_item__should_return_title_with_number_of_copy(title: str):
    assert change_copy_item(title) == f'{title} (2)'

@pytest.mark.parametrize(
        "title, copy_number",
        [
            ("Copy of Test title", 2),
            ("Copy of T3.est 3..2titl3e", 665)
        ]
)
def test__change_copy_item__should_increment_number_of_copy(title: str, copy_number: int):
    assert change_copy_item(f'{title} ({copy_number})') == f'{title} ({copy_number+1})'

@pytest.mark.parametrize(
        "title",
        [
            ("Copy of Test title (a)"),
            ("Copy of T3.est 3..2titl3e (bbb)")
        ]
)
def test__change_copy_item__should_create_number_of_copy_and_ignore_parentheses(title: str):
    assert change_copy_item(title) == f'{title} (2)'
