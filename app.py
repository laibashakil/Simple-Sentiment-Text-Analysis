import streamlit as st
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gensim.summarization import summarize

# Title of the web application
st.title('Simple Sentiment Analyzer')

# Sidebar for user input
st.sidebar.title("Input")
input_option = st.sidebar.radio("Choose Input Option", ("URL", "Text"))

if input_option == "URL":
    input_url = st.sidebar.text_input("Enter the URL of the article you want to analyze", "")
    if input_url:
        # Function to extract article text from a webpage
        def extract_article_text(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            article_text = ''
            for paragraph in soup.find_all('p'):
                article_text += paragraph.get_text() + '\n'
            return article_text

        # Fetch and summarize the article text
        article_text = extract_article_text(input_url)
        summary = summarize(article_text, ratio=0.2)  # Generate summary using Gensim

        st.write("## Summary")
        st.write(summary)  # Display the generated summary

        # Sentiment analysis
        with st.spinner('Analyzing sentiment...'):
            analysis = TextBlob(article_text)
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
        # Summary
        summary = summarize(input_text, ratio=0.2)  # Generate summary using Gensim

        st.write("## Summary")
        st.write(summary)  # Display the generated summary

        # Sentiment analysis
        with st.spinner('Analyzing sentiment...'):
            analysis = TextBlob(input_text)
            polarity = analysis.sentiment.polarity
            if polarity > 0:
                sentiment_comment = 'Positive'
            elif polarity == 0:
                sentiment_comment = 'Neutral'
            else:
                sentiment_comment = 'Negative'

        st.write("## Sentiment Analysis")
        st.write(f"Sentiment Polarity: {polarity:.2f} ({sentiment_comment})")