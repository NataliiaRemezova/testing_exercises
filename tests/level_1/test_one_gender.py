from functions.level_1.one_gender import genderalize


def test__genderalize__should_return_case_male_if_input_is_male():
    assert genderalize("test_m", "test_f", "male") == "test_m"

def test__genderalize__should_return_case_female_if_input_is_female():
    assert genderalize("test_m", "test_f", "female") == "test_f"
