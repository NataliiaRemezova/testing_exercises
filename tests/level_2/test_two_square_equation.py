import math
import pytest
from functions.level_2.two_square_equation import solve_square_equation

@pytest.mark.parametrize(
        "a,b,c,roots",
        [
            (1, 5, 6, [-3.0, -2.0]),
            (1, -5, 6, [3.0, 2.0])
        ]
)
def test__solve_square_equation__should_return_answer_with_two_roots(a: int, b: int, c: int, roots: list[float]):
    assert set(solve_square_equation(a, b, c)) == set(roots)

@pytest.mark.parametrize(
        "a,b,c,roots",
        [
            (2, -8, 8, [2.0]),
            (2, 8, 8, [-2.0])
        ]
)
def test__solve_square_equation__should_return_answer_with_one_root(a: int, b: int, c: int, roots: list[float]):
    assert set(solve_square_equation(a, b, c)) == set(roots)

@pytest.mark.parametrize(
        "a,b,c,roots",
        [
            (1, 5, 7, [None]),
            (1, -3, 7, [None])
        ]
)
def test__solve_square_equation__should_return_no_possible_solution(a: int, b: int, c: int, roots: list[float]):
    assert set(solve_square_equation(a, b, c)) == set(roots)
