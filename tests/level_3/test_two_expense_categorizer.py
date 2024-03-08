import pytest
import decimal
import datetime
from functions.level_3.models import Expense, Currency, BankCard, ExpenseCategory
from functions.level_3.two_expense_categorizer import guess_expense_category, is_string_contains_trigger


test_card = BankCard(last_digits="1234", owner="John Doe")

@pytest.mark.parametrize(
    "expense, expected_category",
    [
        (
            Expense(
                amount=decimal.Decimal("100.00"), 
                currency=Currency.RUB, 
                card=test_card, 
                spent_in="julis cafe", 
                spent_at=datetime.datetime(2024, 1, 1, 10, 00), 
                category=None), 
            ExpenseCategory.BAR_RESTAURANT
            ),
        (
            Expense(
                amount=decimal.Decimal("100.00"), 
                currency=Currency.USD, 
                card=test_card, 
                spent_in="Green Apple Market", 
                spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                category=None), 
            ExpenseCategory.SUPERMARKET
            ),
        (
            Expense(
                amount=decimal.Decimal("100.00"), 
                currency=Currency.EUR, 
                card=test_card, 
                spent_in="netflix", 
                spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                category=None), 
            ExpenseCategory.ONLINE_SUBSCRIPTIONS
            ),
        (
            Expense(
                amount=decimal.Decimal("100.00"), 
                currency=Currency.AMD, 
                card=test_card, 
                spent_in="Alfa-Pharm", 
                spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                category=None), 
            ExpenseCategory.MEDICINE_PHARMACY
            ),
        (
            Expense(
                amount=decimal.Decimal("100.00"), 
                currency=Currency.RUB, 
                card=test_card, 
                spent_in="Moscow Cinema", 
                spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                category=None), 
            ExpenseCategory.THEATRES_MOVIES_CULTURE
            ),
        (
            Expense(
                amount=decimal.Decimal("100.00"), 
                currency=Currency.USD, 
                card=test_card, 
                spent_in="www.taxi.yandex.ru", 
                spent_at=datetime.datetime(2024, 1, 1, 10, 00), 
                category=None), 
            ExpenseCategory.TRANSPORT
            ),
        (
            Expense(
                amount=decimal.Decimal("100.00"), 
                currency=Currency.EUR, 
                card=test_card, 
                spent_in="ABC shop", 
                spent_at=datetime.datetime(2024, 1, 1, 10, 00),
                category=None), 
            None
            ),
    ]
)

def test__guess_expense_category__should_format_and_read_spent_in_input_set_correct_expense_category(expense, expected_category):
    assert guess_expense_category(expense) == expected_category
