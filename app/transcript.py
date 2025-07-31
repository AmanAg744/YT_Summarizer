from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url):
    match = re.search(r"(v=|youtu\.be/)([^&]+)", url)
    return match.group(2) if match else None

def get_transcript(video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([t['text'] for t in transcript])
