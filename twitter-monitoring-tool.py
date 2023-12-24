import os
import requests
import pandas as pd
from textblob import TextBlob

api_key = 'Your-Scraper-APIKEY'

def analyze_tweet(tweet_text, tweet_link, csv_file_path):
    sentiment = TextBlob(tweet_text).sentiment.polarity
    data_sentiment = {'tweet_text': [tweet_text], 'tweet_link': [tweet_link], 'sentiment_score': [sentiment]}

    if os.path.exists(csv_file_path):
        df_sentiment = pd.DataFrame(data_sentiment)
        df_sentiment.to_csv(csv_file_path, mode='a', header=False, index=False)
    else:
        df_sentiment = pd.DataFrame(data_sentiment)
        df_sentiment.to_csv(csv_file_path, index=False)

def scrape_tweets(api_key, query, num_tweets):
    payload = {
        'api_key': api_key,
        'query': query,
        'num': num_tweets
    }

    response = requests.get('https://api.scraperapi.com/structured/twitter/search', params=payload)

    if response.status_code == 200:
        try:
            data = response.json()
            return data.get('organic_results', [])
        except json.decoder.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
    else:
        print(f"API Error: Status Code {response.status_code}")
    return []

search_keyword = 'weapon'
num_tweets_to_fetch = 100

csv_file_path = 'sentiment_analysis_results.csv'

tweets = scrape_tweets(api_key, search_keyword, num_tweets_to_fetch)

if tweets:
    tweet_data = []
    for tweet in tweets:
        tweet_text = tweet['snippet']  # Assuming 'snippet' contains the tweet text
        tweet_link = tweet['link']  # Assuming 'link' contains the tweet link
        tweet_data.append([tweet['position'], tweet['title'], tweet_link, tweet_text])

        # Analyze and store sentiment in a CSV file
        analyze_tweet(tweet_text, tweet_link, csv_file_path)

    columns = ["Position", "Title", "Link", "Snippet"]
    df = pd.DataFrame(tweet_data, columns=columns)

    print("\nTweets:")
    print(df)
else:
    print("No tweets retrieved.")
