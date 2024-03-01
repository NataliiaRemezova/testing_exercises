from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__positive_example():
    test_text = "positive text"
    test_good_words = {"positive"}
    test_bad_words = {"negative"}
    assert check_tweet_sentiment(text = test_text, good_words = test_good_words, bad_words = test_bad_words) == "GOOD"

def test__check_tweet_sentiment__negative_example():
    test_text = "negative text"
    test_good_words = {"positive"}
    test_bad_words = {"negative"}
    assert check_tweet_sentiment(text = test_text, good_words = test_good_words, bad_words = test_bad_words) == "BAD"

def test__check_tweet_sentiment__none_example():
    test_text = "text"
    test_good_words = {"positive"}
    test_bad_words = {"negative"}
    assert check_tweet_sentiment(text = test_text, good_words = test_good_words, bad_words = test_bad_words) == None

def test__check_tweet_sentiment__lower_capital_letters():
    test_text = "Positive Text"
    test_good_words = {"positive"}
    test_bad_words = {"negative"}
    assert check_tweet_sentiment(text = test_text, good_words = test_good_words, bad_words = test_bad_words) == "GOOD"