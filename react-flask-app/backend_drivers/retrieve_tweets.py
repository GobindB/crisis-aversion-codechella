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
        Process the tweets and save them to a PyMySQL AWS database
        """
        print(f"Processing tweet id {tweet.id}\n")
        print(f"Tweet: {tweet.text}\n")
        
        # serve this ID and score to the client
        score = calculate_validity_score(tweet)

        self.insert_into_database(tweet.created_at, tweet.text, tweet.user.screen_name, tweet.id, score)
    
    def insert_into_database(self, created_at, text, screen_name, tweet_id, validity_score):
        db = pymysql.connect(os.getenv("host"), user='admin', passwd=os.getenv("db_pw"), db='twitter', charset="utf8")
        cursor = db.cursor()
        insert_query = "INSERT INTO twitter (tweet_id, user_handle, created_at, text, validity_score) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (tweet_id, screen_name, created_at, text, validity_score))
        db.commit()
        print("\n ADD SUCCESS \n")
        cursor.close()
        db.close()
        return

    def on_error(self, status):
        print(f"Error: {status}")

# get hashtags
def get_tweets(keywords):
    api = create_api()
    tweets_listener = TweetListener(api)
    tweets_listener.keywords = keywords
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

if __name__ == "__main__":
    get_tweets(["Codechella", "Python"])