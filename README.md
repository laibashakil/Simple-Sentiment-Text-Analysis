# Simple Sentiment Analyzer

The Simple Sentiment Analyzer is a natural language processing (NLP) web application built with Streamlit that allows users to analyze the sentiment of articles or text. This application provides a simple and intuitive interface for users to input either a URL of an article or plain text, and it generates a summary of the input along with sentiment analysis.

## Features

-   **Input Options**: Users can choose between two input options: entering a URL of an article or providing plain text directly.
-   **Article Summarization**: For URLs input, the application extracts the article text from the webpage and provides a summary of the content.
-   **Sentiment Analysis**: The application analyzes the sentiment of the input text using TextBlob, categorizing it as Positive, Neutral, or Negative.
-   **User-Friendly Interface**: The Streamlit app offers a clean and intuitive user interface, with input options conveniently placed in the sidebar.

## Dependencies

-   Streamlit: For building the web application interface.
-   Beautiful Soup: For web scraping and extracting article text from webpages.
-   TextBlob: For sentiment analysis of the input text.
-   Requests: For making HTTP requests to fetch webpage content.

## Installation

1.  Clone the repository to your local machine:
    
    bashCopy code
    
    `git clone https://github.com/laibashakil/simple-sentiment-analyzer.git` 
    
2.  Navigate to the project directory:
    
    bashCopy code
    
    `cd simple-sentiment-analyzer` 
    
3.  Install the required Python dependencies using pip:
    
    bashCopy code
    
    `pip install -r requirements.txt` 
    

## Usage

1.  Run the Streamlit app locally:
    
    bashCopy code
    
    `streamlit run app.py` 
    
2.  Access the application in your web browser by navigating to the provided local URL.
    
3.  Choose an input option (URL or Text) in the sidebar.
    
4.  Enter the URL of an article or provide plain text for analysis.
    
5.  View the summary of the input and the sentiment analysis results displayed on the page.
    

## Example

Below are sccreenshots demonstrating the usage of the Simple Sentiment Analyzer:
![image](https://github.com/laibashakil/Simple-Sentiment-Text-Analysis/assets/96187426/9065adca-437f-4c61-9c06-ce70b374795c)
![image](https://github.com/laibashakil/Simple-Sentiment-Text-Analysis/assets/96187426/498c7dd1-0973-4f44-8367-a4dd3a94fc0c)

## Contributing

Contributions to the Simple Sentiment Analyzer project are welcome! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them to your branch.
4.  Push your branch to your fork.
5.  Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
