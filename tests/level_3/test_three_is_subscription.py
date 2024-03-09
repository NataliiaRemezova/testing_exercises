import pytest
import collections
import decimal
import datetime
from statistics import mean
from functions.level_3.models import Expense, Currency, BankCard, ExpenseCategory
from functions.level_3.three_is_subscription import is_subscription


test_card = BankCard(last_digits="1234", owner="John Doe")

@pytest.mark.parametrize(
    "expense, history, expected_result",
    [
        (
            Expense(
                    amount=decimal.Decimal("10.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="AppStore",
                    spent_at=datetime.datetime(2024, 2, 1, 10, 00),
                    category=ExpenseCategory.SUPERMARKET
                ),
            [
                Expense(
                    amount=decimal.Decimal("10.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="AppStore",
                    spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                    category=ExpenseCategory.SUPERMARKET
                ),
                Expense(
                    amount=decimal.Decimal("10.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="AppStore",
                    spent_at=datetime.datetime(2024, 2, 1, 10, 00),
                    category=ExpenseCategory.SUPERMARKET
                ),
            ],
            False,
        ),
        (
            Expense(
                    amount=decimal.Decimal("10.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="AppStore",
                    spent_at=datetime.datetime(2024, 3, 1, 10, 00),
                    category=ExpenseCategory.SUPERMARKET
                ),
            [
                Expense(
                    amount=decimal.Decimal("10.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="AppStore",
                    spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                    category=ExpenseCategory.SUPERMARKET
                ),
                Expense(
                    amount=decimal.Decimal("10.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="AppStore",
                    spent_at=datetime.datetime(2024, 2, 1, 10, 00),
                    category=ExpenseCategory.SUPERMARKET
                ),
                Expense(
                    amount=decimal.Decimal("10.00"),
                    currency=Currency.USD,
                    card=test_card,
                    spent_in="AppStore",
                    spent_at=datetime.datetime(2024, 3, 1, 10, 00),
                    category=ExpenseCategory.SUPERMARKET
                )
            ],
            True,
        ),
    ]
)
def test__is_subscription__should_check_number_of_payments_in_payment_history(expense, history, expected_result):
    assert is_subscription(expense, history) == expected_result
    