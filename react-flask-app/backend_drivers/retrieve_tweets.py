import tweepy
import pymysql
import dotenv
import json, string, os
from config import create_api
from misinformation_model import calculate_validity_score


class TweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.keywords = []

    def on_status(self, tweet):
        """
        Process the tweets and save them to a flask database???
        """
        print(f"Processing tweet id {tweet.id}\n")
        print(f"Tweet: {tweet.text}\n")
        
        # TODO: pass tweet content to misinformation module and store tweet ID
        # and validity score in a buffer for n number of tweets per request,
        # serve this ID and score to the client
        score = calculate_validity_score(tweet)

        self.store_data(tweet, score)
    
    def store_data(tweet, validity_score):
        db = pymysql.connect(os.getenv("host"), user='admin', passwd=os.getenv("db_pw"), db='twitter', charset="utf8")
        cursor = db.cursor()
        insert_query = "INSERT INTO twitter (tweet_id, user_handle, created_at, text, validity_score) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (tweet.id, tweet.user.screen_name, tweet.created_at, tweet.text, validity_score))
        db.commit()
        print("\n ADD SUCCESS \n")
        cursor.close()
        db.close()
        return

    def on_error(self, status):
        print(f"Error: {status}")

def get_tweets(keywords):
    api = create_api()
    tweets_listener = TweetListener(api)
    tweets_listener.keywords = keywords
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

if __name__ == "main":
    get_tweets(["Codechella"])