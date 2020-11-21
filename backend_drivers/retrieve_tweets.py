import tweepy
from config import create_api
import json, string

class TweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.filtered_responses = {}

    def on_status(self, tweet):
        print(f"Processing tweet id {tweet.id}\n")
        print(f"Tweet: {tweet.text}\n")
        self.filtered_responses[tweet.id] = tweet.text
        
        assert "aid" in string.lower(tweet.text)

    def on_error(self, status):
        print(f"Error: {status}")

def get_tweets(keywords):
    api = create_api()
    tweets_listener = TweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])
    if len(tweets_listener.filtered_responses) == 3:
        return tweets_listener.filtered_responses
