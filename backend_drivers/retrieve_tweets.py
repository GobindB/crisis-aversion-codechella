import tweepy
from config import create_api
import json

class TweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api

    def on_status(self, tweet):
        print(f"Processing tweet id {tweet.id}\n")
        print(f"Tweet: {tweet.text}\n")

    def on_error(self, status):
        print(f"Error: {status}")

def main(keywords):
    api = create_api()
    tweets_listener = TweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])
    # return 5 tweets

if __name__ == "__main__":
    main(["Python", "Tweepy"])