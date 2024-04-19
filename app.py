import streamlit as st
from newspaper import Article
from textblob import TextBlob
import nltk
import lxml

# Download nltk resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Title of the web application
st.title('Simple Sentiment Analyzer')

# Sidebar for user input
st.sidebar.title("Input")
input_option = st.sidebar.radio("Choose Input Option", ("URL", "Text"))

if input_option == "URL":
    input_url = st.sidebar.text_input("Enter the URL of the article you want to analyze", "")
    if input_url:
        # Fetch and parse the article
        article = Article(input_url)
        article.download()
        article.parse()

        # Summary
        st.write("## Summary")
        st.write(article.text[:500])  # Display the first 500 characters as summary

        # Sentiment analysis
        with st.spinner('Analyzing sentiment...'):
            analysis = TextBlob(article.text)
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
        st.write("## Summary")
        st.write(input_text[:500])  # Display the first 500 characters as summary

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