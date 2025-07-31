from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def summarize_text(text):
    return summarizer(text[:1000], max_length=150, min_length=40, do_sample=False)[0]['summary_text']
