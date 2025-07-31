from app.summarizer import summarize_text

def test_summarize_text():
    long_text = "This is a sample sentence. " * 100
    summary = summarize_text(long_text)
    assert isinstance(summary, str)
