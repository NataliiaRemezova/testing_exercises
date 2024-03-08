import datetime
import decimal
import pytest
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense

@pytest.mark.parametrize(
        "cards,sms_text,expected_card",
        [
            ([
                BankCard(last_digits="0123", owner="John Doe"),
                BankCard(last_digits="4567", owner="Anna Smith"),
            ], "50.00 EUR, 45670123 03.03.24 10:00 SAMPLE_CAFE authcode 234567",
            0),
            ([
                BankCard(last_digits="0123", owner="John Doe"),
                BankCard(last_digits="4567", owner="Anna Smith"),
            ], "150.00 EUR, 45674567 03.03.24 10:00 SAMPLE_CAFE authcode 234567",
            1),
        ]
)
def test__parse_ineco_expense__should_select_correct_card(cards: list[BankCard], sms_text: str, expected_card: int): 
    sms = SmsMessage(text=sms_text, author="Sample Bank", sent_at=datetime.datetime.now())
    
    expense = parse_ineco_expense(sms, cards)
    assert expense.card == cards[expected_card]

@pytest.mark.parametrize(
        "cards,sms_text",
        [
            ([
                BankCard(last_digits="0123", owner="John Doe"),
                BankCard(last_digits="4567", owner="Anna Smith"),
            ], "50.00 EUR, some details 03.03.24 10:00 SAMPLE_CAFE authcode 234567"),
            ([
                BankCard(last_digits="0123", owner="John Doe"),
                BankCard(last_digits="4567", owner="Anna Smith"),
            ], "3350.00 EUR, some details 03.03.24 10:00 SAMPLE_CAFE authcode 2334567"),
        ]
)
def test__parse_ineco_expense__should_raise_index_error_when_incorrect_card_data(cards: list[BankCard], sms_text: str):
    sms = SmsMessage(text=sms_text, author="Sample Bank", sent_at=datetime.datetime.now())
    
    with pytest.raises(IndexError): 
        parse_ineco_expense(sms, cards)

@pytest.mark.parametrize(
        "cards,sms_text",
        [
            ([
                BankCard(last_digits="0123", owner="John Doe"),
                BankCard(last_digits="4567", owner="Anna Smith"),
            ], "Incorrect sms message"),
            ([
                BankCard(last_digits="0123", owner="John Doe"),
                BankCard(last_digits="4567", owner="Anna Smith"),
            ], "test 4 92 0000000ffffff kwwwwwww"),
        ]
)
def test__parse_ineco_expense__should_raise_value_error_when_incorrect_sms_format(cards: list[BankCard], sms_text: str):
    sms = SmsMessage(text=sms_text, author="Sample Bank", sent_at=datetime.datetime.now())
    
    with pytest.raises(ValueError): 
        parse_ineco_expense(sms, cards)
        