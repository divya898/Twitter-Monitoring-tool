# Twitter Sentiment Analysis Scraper

This Python script performs sentiment analysis on tweets retrieved from Twitter based on a specific keyword using the Scraper API. The sentiment analysis results are stored in a CSV file, including tweet text, tweet link, and sentiment score.

## Setup

1. **Install Dependencies:**
   - Make sure you have Python installed on your machine.
   - Install required Python packages using the following command:

     ```bash
     pip install requests pandas textblob
     ```

2. **API Key:**
   - Get an API key from Scraper API (https://www.scraperapi.com/).
   - Replace the placeholder `c89676733a675670ce9b06bd0a79cda7` with your actual API key in the script.

3. **Run the Script:**
   - Adjust the `search_keyword` variable in the script to set the keyword you want to search for.
   - Run the script:

     ```bash
     python script_name.py
     ```

## Output

The script outputs the retrieved tweets and their sentiment analysis results to the console. Additionally, it appends the sentiment analysis results to a CSV file named `sentiment_analysis_results.csv` in the script's directory.

## Dependencies

- `requests`: For making HTTP requests to the Scraper API.
- `pandas`: For handling and manipulating data in tabular format.
- `textblob`: For sentiment analysis.

## Note

- Make sure to comply with Scraper API's terms of service when using their service.

## Author

Divya Prakash Srivastava

