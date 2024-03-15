from functions.level_2.three_first import first, NOT_SET
import pytest

@pytest.mark.parametrize(
        "items, default, expected_value",
        [
            ([1, 2, 3], 2, 1),
            ([-3, 2, 3], 2, -3)
        ]
)
def test__first__should_return_first_element_of_items(items: list[int], default: int, expected_value: int):
    assert first(items = items, default = default) == expected_value

@pytest.mark.parametrize(
        "items, default, expected_value",
        [
            (None, -2, -2),
            (None, 5, 5)
        ]
)
def test__first__should_return_default(items: list[int], default: int, expected_value: int):
    assert first(items = items, default = default) == expected_value

def test__first__should_return_default_none():
    assert first(items = None, default = None) == None

def test__first__should_raise_attribute_error():
    with pytest.raises(AttributeError):
        first(items = None, default = NOT_SET)
