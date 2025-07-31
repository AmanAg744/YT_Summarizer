import streamlit as st
from app.transcript import get_transcript
from app.summarizer import summarize_text
from app.sentiment import analyze_sentiment

st.title("🎥 YouTube Video Summarizer & Sentiment Dashboard")

video_url = st.text_input("Enter YouTube Video URL:")

if st.button("Analyze"):
    try:
        with st.spinner("Fetching transcript..."):
            transcript = get_transcript(video_url)
        st.success("Transcript fetched!")

        with st.spinner("Summarizing..."):
            summary = summarize_text(transcript)
        st.success("Summary generated!")

        sentiment = analyze_sentiment(summary)

        st.subheader("📄 Summary")
        st.write(summary)

        st.subheader("📊 Sentiment")
        st.success(sentiment)

    except Exception as e:
        st.error(f"Error: {e}")
