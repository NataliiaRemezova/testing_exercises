from functions.level_1.one_gender import genderalize


def test_genderalize_case_male():
    assert genderalize("test_m", "test_f", "male") == "test_m"

def test_genderalize_case_female():
    assert genderalize("test_m", "test_f", "female") == "test_f"
