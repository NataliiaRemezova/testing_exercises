import pytest
from functions.level_2.four_sentiment import check_tweet_sentiment

@pytest.mark.parametrize(
    "test_text, test_good_words, test_bad_words, expected_result",
    [
        ("positive text", {"positive"}, {"negative"}, "GOOD"),
        ("negative text", {"positive"}, {"negative"}, "BAD"),
        ("text", {"positive"}, {"negative"}, None),
        ("Positive Text", {"positive"}, {"negative"}, "GOOD"),
    ]
)
def test__check_tweet_sentiment__should_find_positive_negative_or_none_sentiment_and_handle_capitalization(test_text, test_good_words, test_bad_words, expected_result):
    assert check_tweet_sentiment(text=test_text, good_words=test_good_words, bad_words=test_bad_words) == expected_result
