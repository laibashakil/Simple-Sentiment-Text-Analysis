
# Simple Sentiment Text Analysis

Simple Sentiment Text Analysis is a Python web application built with Streamlit, designed for analyzing the sentiment of text data. It provides users with the ability to input either a URL of an article or directly enter text for sentiment analysis. The application extracts the text, generates a summary, and performs sentiment analysis on the input data.

## Features

-   **Text Summarization**: Utilizes NLTK to generate a summary of the input text based on word frequencies.
-   **Sentiment Analysis**: Employs NLTK's Vader Sentiment Analyzer to determine the sentiment polarity of the input text.
-   **Web Scraping**: Allows users to input a URL to fetch the text content from a webpage for analysis.
-   **User-friendly Interface**: Implemented using Streamlit, providing an intuitive and interactive user experience.

## Installation

To run the application locally, follow these steps:

1.  Clone the repository:
    
    `git clone https://github.com/your-username/simple-sentiment-text-analysis.git` 
    
2.  Navigate to the project directory:
    
    `cd simple-sentiment-text-analysis` 
    
3.  Install the dependencies:
   
    `pip install -r requirements.txt` 
    
5.  Run the Streamlit app:
    
    `streamlit run app.py` 
    
6.  Access the application in your browser at `http://localhost:8501`.
    

## Usage

Once the application is running, users can interact with it through a web interface. Here's how to use the application:

1.  Choose Input Option: Select whether to input a URL or text directly.
2.  Enter Input: Depending on the selected option, provide a URL or text input.
3.  Analyze: Click on the "Analyze" button to generate the summary and sentiment analysis results.

## Dependencies

The project relies on the following Python packages:

-   Streamlit
-   Requests
-   Beautiful Soup
-   NLTK

These dependencies are listed in the `requirements.txt` file for easy installation.

## Screenshots
![image](https://github.com/laibashakil/Simple-Sentiment-Text-Analysis/assets/96187426/8af94141-3e86-4ec1-8528-35bba705a84c)
![image](https://github.com/laibashakil/Simple-Sentiment-Text-Analysis/assets/96187426/d5798474-71e4-4964-8ad1-9047f6d9d9d6)

## Contributing

Contributions to the project are welcome! If you have any ideas for improvements, new features, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
