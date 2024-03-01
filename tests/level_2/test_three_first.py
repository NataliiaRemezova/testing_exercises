from functions.level_2.three_first import first, NOT_SET
import pytest


def test__first__return_first_element_of_items():
    assert first(items = [1, 2, 3], default = 2) == 1

def test__first__return_default():
    assert first(items = None, default = 2) == 2

def test__first__return_default_none():
    assert first(items = None, default = None) == None

def test__first__raise_attribute_error():
    with pytest.raises(AttributeError):
        first(items = None, default = NOT_SET)
