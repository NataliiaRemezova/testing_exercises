from functions.level_1.one_gender import genderalize
import pytest


def test__genderalize__should_return_case_male_if_input_is_male():
    assert genderalize("test_m", "test_f", "male") == "test_m"

@pytest.mark.parametrize(
        "gender",
        [
            ("female"),
            ("unknown")
        ]
)
def test__genderalize__should_return_case_female_if_input_is_not_male(gender: str):
    assert genderalize("test_m", "test_f", gender) == "test_f"
