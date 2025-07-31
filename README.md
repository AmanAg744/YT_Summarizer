YouTube Video Summarizer & Sentiment Dashboard
==============================================

A complete Python-based Streamlit application that takes any YouTube video URL, extracts the transcript, summarizes it using a transformer model, and performs sentiment analysis. The project includes unit tests using Pytest and continuous integration using GitHub Actions. It is fully deployable via Streamlit Cloud.

FEATURES
--------

*   Paste a YouTube URL and fetch the video transcript automatically
    
*   Generate a short, clean summary using the T5-small transformer model
    
*   Analyze the sentiment of the transcript (positive, neutral, or negative)
    
*   Beautiful, minimal interface using Streamlit
    
*   Tested with Pytest (unit tests for all key modules)
    
*   Continuous Integration using GitHub Actions
    
*   Deployable in one click to Streamlit Cloud
    

WHY SENTIMENT ANALYSIS?
-----------------------

Summarization tells users _what_ the content is, while sentiment tells them _how_ it feels. This emotional context is valuable for:

*   Understanding the tone (serious, joyful, controversial, etc.)
    
*   Helping users filter or prioritize content
    
*   Adding metadata for content recommendation engines
    
*   Providing emotional analytics for marketers, educators, or content reviewers
    

TECH STACK
----------

*   Python (3.9)
    
*   Streamlit (Frontend + Deployment)
    
*   youtube-transcript-api (Transcript extraction)
    
*   Hugging Face Transformers (t5-small for summarization)
    
*   TextBlob (Sentiment analysis)
    
*   Pytest (Testing)
    
*   GitHub Actions (CI/CD)
    

PROJECT STRUCTURE
-----------------

youtube\_summarizer/├── app/│ ├── transcript.py -> Extracts YouTube transcript│ ├── summarizer.py -> Summarizes transcript text│ └── sentiment.py -> Performs sentiment analysis├── tests/│ ├── test\_transcript.py -> Unit tests for transcript logic│ ├── test\_summarizer.py -> Unit tests for summarizer│ └── test\_sentiment.py -> Unit tests for sentiment logic├── streamlit\_app.py -> Main application file├── requirements.txt -> Project dependencies└── .github/└── workflows/└── test-and-deploy.yml -> CI workflow using GitHub Actions

HOW TO RUN LOCALLY
------------------

1.  Clone the repository
    
2.  Create and activate a virtual environment
    
3.  Install dependenciespip install -r requirements.txt
    
4.  Start the Streamlit appstreamlit run streamlit\_app.py
    

DEPLOYMENT (STREAMLIT CLOUD)
----------------------------

1.  Push the code to a GitHub repository
    
2.  Go to https://streamlit.io/cloud
    
3.  Click "New App" → Connect to GitHub
    
4.  Set the main file as streamlit\_app.py
    
5.  Click "Deploy"
    

CI/CD WITH GITHUB ACTIONS
-------------------------

The project includes a GitHub Actions workflow file that:

*   Runs Pytest on every push to main
    
*   Ensures all modules work as expected before merging or deploying
    

CI Workflow: .github/workflows/test-and-deploy.yml

TESTING
-------

To run all tests locally:

pytest tests/

Pytest covers:

*   Transcript extraction
    
*   Summary generation
    
*   Sentiment classification
    

FUTURE IMPROVEMENTS
-------------------

*   Support longer transcripts using chunking
    
*   Use BERT or RoBERTa for more accurate sentiment analysis
    
*   Store transcript/summary/sentiment history in PostgreSQL
    
*   Add user login and personalized dashboard for saved results
    

AUTHOR
------

Aman AgarwalGitHub: [https://github.com/AmanAg744](https://github.com/your-username)
