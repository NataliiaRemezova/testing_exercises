import pytest
import decimal
import datetime
from statistics import mean
from functions.level_3.models import Expense, Currency, BankCard, ExpenseCategory
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


test_card = BankCard(last_digits="1234", owner="John Doe")

@pytest.mark.parametrize(
    "expenses, expected_average",
    [
        (
            [
                Expense(
                    amount=decimal.Decimal("50.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="Supermarket",
                    spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                    category=ExpenseCategory.SUPERMARKET
                ),
                Expense(
                    amount=decimal.Decimal("30.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="Cafe",
                    spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                    category=ExpenseCategory.BAR_RESTAURANT
                ),
                Expense(
                    amount=decimal.Decimal("20.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="Bookshop",
                    spent_at=datetime.datetime(2024, 1, 2, 10, 00),
                    category=ExpenseCategory.THEATRES_MOVIES_CULTURE
                ),
            ],
            mean([decimal.Decimal("80.00"), decimal.Decimal("20.00")]),
        ),
        (
            [
                Expense(
                    amount=decimal.Decimal("100.00"),
                    currency=Currency.EUR,
                    card=test_card,
                    spent_in="Taxi",
                    spent_at=datetime.datetime(2024, 1, 3, 10, 00),
                    category=ExpenseCategory.TRANSPORT
                ),
            ],
            decimal.Decimal("100.00"),
        ),
    ]
)

def test__calculate_average_daily_expenses__should_calculate_and_compare_expected_average_per_day(expenses, expected_average):
    calculated_average = calculate_average_daily_expenses(expenses)
    assert calculated_average == expected_average
    