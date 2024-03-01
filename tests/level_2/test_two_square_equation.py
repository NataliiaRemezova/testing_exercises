import math
from functions.level_2.two_square_equation import solve_square_equation

def test__solve_square_equation__negative_numbers():
    assert solve_square_equation(square_coefficient = 1, linear_coefficient = 5, const_coefficient = 6) == (-3.0, -2.0)

# Problem with answer recognition in solve_square_equation(): 
# if the sequence of numbers is changed, which does not affect the answer of the equation, 
# e.g. (-2.0, -3.0) instead of (-3.0, -2.0), the test fails with an error
def test__solve_square_equation__answer_sequence_changed():
    assert solve_square_equation(square_coefficient = 1, linear_coefficient = 5, const_coefficient = 6) != (-2.0, -3.0)

def test__solve_square_equation__answer_positive_numbers():
    assert solve_square_equation(square_coefficient = 1, linear_coefficient = -5, const_coefficient = 6) == (2.0, 3.0)

def test__solve_square_equation__no_possible_solution():
    assert solve_square_equation(square_coefficient = 1, linear_coefficient = 4, const_coefficient = 5) == (None, None)
