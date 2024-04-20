import streamlit as st
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk.data
import nltk

# Download NLTK resources (only required once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Title of the web application
st.title('Simple Sentiment Analyzer')

# Sidebar for user input
st.sidebar.title("Input")
input_option = st.sidebar.radio("Choose Input Option", ("URL", "Text"))

def extract_text(input_source):
    if input_source == "URL":
        input_url = st.sidebar.text_input("Enter the URL of the article you want to analyze", "")
        if input_url:
            # Function to extract article text from a webpage
            response = requests.get(input_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            article_text = ''
            for paragraph in soup.find_all('p'):
                article_text += paragraph.get_text() + '\n'
            return article_text
    else:
        input_text = st.sidebar.text_area("Enter the text you want to analyze", "")
        if input_text:
            return input_text

# Extract text based on user input
article_text = extract_text(input_option)

if article_text:
    # Tokenize the text into sentences
    sentences = sent_tokenize(article_text)

    # Tokenize words and remove stopwords
    tokenizer = RegexpTokenizer(r'\w+')
    words = [word.lower() for sentence in sentences for word in tokenizer.tokenize(sentence)]
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    # Calculate word frequencies
    word_freq = FreqDist(words)

    # Calculate sentence scores based on word frequencies
    sentence_scores = {sentence: sum([word_freq[word] for word in word_tokenize(sentence.lower()) if word not in stop_words]) for sentence in sentences}

    # Sort sentences by score in descending order
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)

    # Generate summary by selecting top sentences
    summary_sentences = sorted_sentences[:3]  # Adjust the number of sentences for summary length
    summary = ' '.join(sentence[0] for sentence in summary_sentences)

    # Display summary
    st.write("## Summary")
    st.write(summary)

    # Sentiment analysis
    st.write("## Sentiment Analysis")
    sid = SentimentIntensityAnalyzer()
    compound_score = sid.polarity_scores(article_text)['compound']

    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    st.write(f"Compound Sentiment Score: {compound_score:.2f} ({sentiment})")
