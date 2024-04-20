import streamlit as st
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.summarization import summarize
from textblob import TextBlob

# Download NLTK resources (run this once)
nltk.download("punkt")
nltk.download("stopwords")

# Function to extract article text from a webpage
def extract_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article_text = ''
    for paragraph in soup.find_all('p'):
        article_text += paragraph.get_text() + '\n'
    return article_text

# Function to preprocess text
def preprocess_text(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words("english"))

    words = [word_tokenize(sentence.lower()) for sentence in sentences]
    words = [[word for word in sentence if word.isalnum() and word not in stop_words] for sentence in words]

    return sentences, words

# Title of the web application
st.title('Simple Sentiment Analyzer')

# Sidebar for user input
st.sidebar.title("Input")
input_option = st.sidebar.radio("Choose Input Option", ("URL", "Text"))

if input_option == "URL":
    input_url = st.sidebar.text_input("Enter the URL of the article you want to analyze", "")
    if input_url:
        # Fetch and summarize the article text
        article_text = extract_article_text(input_url)
        sentences, words = preprocess_text(article_text)
        summary = summarize(article_text, ratio=0.2)  # Using Gensim to summarize the text

        st.write("## Summary")
        st.write(summary)  # Display the Gensim summary

        # Sentiment analysis
        with st.spinner('Analyzing sentiment...'):
            analysis = TextBlob(article_text)  # Analysis based on the whole text
            polarity = analysis.sentiment.polarity
            if polarity > 0:
                sentiment_comment = 'Positive'
            elif polarity == 0:
                sentiment_comment = 'Neutral'
            else:
                sentiment_comment = 'Negative'

        st.write("## Sentiment Analysis")
        st.write(f"Sentiment Polarity: {polarity:.2f} ({sentiment_comment})")

else:
    input_text = st.sidebar.text_area("Enter the text you want to analyze", "")
    if input_text:
        # Preprocess text and summarize
        sentences, words = preprocess_text(input_text)
        summary = summarize(input_text, ratio=0.2)  # Using Gensim to summarize the text

        st.write("## Summary")
        st.write(summary)  # Display the Gensim summary

        # Sentiment analysis
        with st.spinner('Analyzing sentiment...'):
            analysis = TextBlob(input_text)  # Analysis based on the whole text
            polarity = analysis.sentiment.polarity
            if polarity > 0:
                sentiment_comment = 'Positive'
            elif polarity == 0:
                sentiment_comment = 'Neutral'
            else:
                sentiment_comment = 'Negative'

        st.write("## Sentiment Analysis")
        st.write(f"Sentiment Polarity: {polarity:.2f} ({sentiment_comment})")