from app.sentiment import analyze_sentiment

def test_analyze_sentiment():
    assert analyze_sentiment("I love it") == "Positive"
    assert analyze_sentiment("I hate it") == "Negative"
    assert analyze_sentiment("This is a pen") == "Neutral"
