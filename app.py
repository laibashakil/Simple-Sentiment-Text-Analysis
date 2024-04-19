import nltk
nltk.download('punkt')

import streamlit as st
from newspaper import Article
from textblob import TextBlob
import nltk

# Title of the web application
st.title('Simple Sentiment Analyzer')

# Sidebar for user input
st.sidebar.title("URL Input")
input_url = st.sidebar.text_input("Enter the URL of the article you want to analyze", "")

def fetch_article(url):
    """ Fetch and parse the article. """
    article = Article(url)
    article.download()
    article.parse()
    return article

def summarize_text(text):
    """ Use TextBlob for extracting summary of the text. """
    blob = TextBlob(text)
    return '\n'.join(blob.sentences[:5])  # Adjusting number for length of summary

def analyze_sentiment(text):
    """ Analyze the sentiment of the text. """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return polarity, 'Positive'
    elif polarity == 0:
        return polarity, 'Neutral'
    else:
        return polarity, 'Negative'

if input_url:
    # Processing
    with st.spinner('Fetching and analyzing the article...'):
        article = fetch_article(input_url)
        summary = summarize_text(article.text)
        polarity, sentiment = analyze_sentiment(article.text)
    
    # Display results
    st.write("## Summary")
    st.write(summary)
    
    st.write("## Sentiment Analysis")
    st.write(f"Sentiment Polarity: {polarity:.2f} ({sentiment})")
else:
    st.write("Please enter a URL in the sidebar to begin.")
