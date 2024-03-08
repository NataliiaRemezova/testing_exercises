import math
import pytest
from functions.level_2.two_square_equation import solve_square_equation

@pytest.mark.parametrize(
        "square_coefficient,linear_coefficient,const_coefficient,expected_set",
        [
            (1, 5, 6, {-3.0, -2.0}),
            (2, 8, 8, {-2.0})
        ]
)
def test__solve_square_equation__should_return_answer_with_negative_numbers(square_coefficient: int, linear_coefficient: int, const_coefficient: int, expected_set: set[float]):
    assert set(solve_square_equation(square_coefficient = square_coefficient, linear_coefficient = linear_coefficient, const_coefficient = const_coefficient)) == expected_set

@pytest.mark.parametrize(
        "square_coefficient,linear_coefficient,const_coefficient,expected_set",
        [
            (1, -5, 6, {3.0, 2.0}),
            (2, -8, 8, {2.0})
        ]
)
def test__solve_square_equation__should_return_answer_with_positive_numbers(square_coefficient: int, linear_coefficient: int, const_coefficient: int, expected_set: set[float]):
    assert set(solve_square_equation(square_coefficient = square_coefficient, linear_coefficient = linear_coefficient, const_coefficient = const_coefficient)) == expected_set

@pytest.mark.parametrize(
        "square_coefficient,linear_coefficient,const_coefficient,expected_set",
        [
            (1, 5, 7, {None}),
            (1, -3, 7, {None})
        ]
)
def test__solve_square_equation__should_return_no_possible_solution(square_coefficient: int, linear_coefficient: int, const_coefficient: int, expected_set: set[float]):
    assert set(solve_square_equation(square_coefficient = square_coefficient, linear_coefficient = linear_coefficient, const_coefficient = const_coefficient)) == expected_set
