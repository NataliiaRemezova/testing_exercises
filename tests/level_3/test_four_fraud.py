import pytest
import decimal
import datetime
from functions.level_3.models import Expense, Currency, BankCard, ExpenseCategory
from functions.level_3.four_fraud import find_fraud_expenses


test_card = BankCard(last_digits="1234", owner="John Doe")

@pytest.mark.parametrize(
    "history, expected_frauds",
    [
        (
            [
                Expense(
                    amount=decimal.Decimal("100.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="Fraud shop",
                    spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                    category=None
                ) for _ in range(4)
                ] + [
                Expense(
                    amount=decimal.Decimal("30.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="Cafe",
                    spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                    category=ExpenseCategory.BAR_RESTAURANT
                )
            ],
            [
                Expense(
                    amount=decimal.Decimal("100.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="Fraud shop",
                    spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                    category=None
                ) for _ in range(4)
            ]
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
                Expense(
                    amount=decimal.Decimal("50.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="Supermarket",
                    spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                    category=ExpenseCategory.SUPERMARKET
                ),
                Expense(
                    amount=decimal.Decimal("20.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="Bookshop",
                    spent_at=datetime.datetime(2024, 1, 2, 10, 00),
                    category=ExpenseCategory.THEATRES_MOVIES_CULTURE
                )
            ],
            []
        ),
    ]
)

def test__find_fraud_expenses__should_find_repetative_expenses_and_detect_fraud(history, expected_frauds):
    assert find_fraud_expenses(history) == expected_frauds
