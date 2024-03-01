import datetime
import decimal
import pytest
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense

def test__parse_ineco_expense__should_return_expense_object():
    sms_text = "100.00 EUR, 12340123 01.01.24 15:30 SAMPLE_SHOP authcode 123456"
    sms = SmsMessage(text=sms_text, author="Sample Bank", sent_at=datetime.datetime.now())
    cards = [BankCard(last_digits="0123", owner="John Doe")]
    
    expected_expense = Expense(
        amount=decimal.Decimal("100.00"),
        card=cards[0],
        spent_in="SAMPLE_SHOP",
        spent_at=datetime.datetime.strptime("01.01.24 15:30", "%d.%m.%y %H:%M"),
    )
    
    assert parse_ineco_expense(sms, cards) == expected_expense

def test__parse_ineco_expense__should_select_correct_card():
    cards = [
        BankCard(last_digits="0123", owner="John Doe"),
        BankCard(last_digits="4567", owner="Anna Smith"),
    ]    
    sms_text = "50.00 EUR, 45670123 03.03.24 10:00 SAMPLE_CAFE authcode 234567"
    sms = SmsMessage(text=sms_text, author="Sample Bank", sent_at=datetime.datetime.now())
    
    expense = parse_ineco_expense(sms, cards)
    assert expense.card == cards[0]

def test__parse_ineco_expense__should_raise_index_error_when_incorrect_card_data():
    cards = [
        BankCard(last_digits="0123", owner="John Doe"),
        BankCard(last_digits="4567", owner="Anna Smith"),
    ]    
    sms_text = "50.00 EUR, some details 03.03.24 10:00 SAMPLE_CAFE authcode 234567"
    sms = SmsMessage(text=sms_text, author="Sample Bank", sent_at=datetime.datetime.now())
    
    with pytest.raises(IndexError): 
        parse_ineco_expense(sms, cards)

def test__parse_ineco_expense__should_raise_value_error_when_incorrect_sms_format():
    cards = [
        BankCard(last_digits="0123", owner="John Doe"),
        BankCard(last_digits="4567", owner="Anna Smith"),
    ]    
    sms_text = "Incorrect sms message"
    sms = SmsMessage(text=sms_text, author="Sample Bank", sent_at=datetime.datetime.now())
    
    with pytest.raises(ValueError): 
        parse_ineco_expense(sms, cards)