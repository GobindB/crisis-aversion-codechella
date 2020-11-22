import tweepy
import pymysql
import dotenv
import logging
import json
import string
import os
import time
from config import create_api
from misinformation_model import calculate_validity_score

logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

# gets 10 most recent tweets according to filter parameters


class TweetListener(tweepy.StreamListener):
    def __init__(self, api, model, keywords):
        self.api = api
        self.responses = []
        self.keywords = keywords
        self.model = model
        self.num_tweets = 0
        self.limit = 1

    def increment_num_tweets(self):
        self.num_tweets += 1

    def on_status(self, tweet):
        """
        Process the tweets and save them to a PyMySQL AWS database
        """
        logging.info(f"Processing tweet id {tweet.id}\n")
        logging.info(f"Tweet: {tweet.text}\n")

        # assume keyword in text due to high frequency usage in crisis event
        if any(word in tweet.text for word in self.keywords):
            # serve this ID and score to the client
            score = calculate_validity_score(tweet, self.model)

            # TODO: extended text
            self.insert_into_database(
                tweet.created_at, tweet.text, tweet.user.screen_name, tweet.id, score)

            response = {'id': tweet.id, 'handle': tweet.user.screen_name,
                        'created_at': tweet.created_at, 'text': tweet.text, 'validity_score': float(score)}
            self.responses.append(response)

            self.increment_num_tweets()
            if self.num_tweets < self.limit:
                return True
            else:
                return False

    # save to database for data analytics
    def insert_into_database(self, created_at, text, screen_name, tweet_id, validity_score):
        db = pymysql.connect(os.getenv("host"), user='admin', passwd=os.getenv(
            "db_pw"), db='twitter', charset="utf8")
        cursor = db.cursor()
        insert_query = "INSERT INTO twitter (tweet_id, user_handle, created_at, text, validity_score) VALUES (%s, %s, %s, %s, %s)"
        final_score = float(validity_score[0][0])
        cursor.execute(insert_query, (tweet_id, screen_name,
                                      created_at, text, final_score))
        db.commit()
        logging.info("Data added to AWS RDBMS succesfuly")
        cursor.close()
        db.close()
        return

    def on_error(self, status):
        logging.error(f"Error: {status}")

# get hashtags
# this may not work because the filter may not be able to get all together


def get_tweets(keywords, languages, locations, model):
    api = create_api()
    tweets_listener = TweetListener(api, model, keywords)
    tweet_stream = tweepy.Stream(
        api.auth, tweets_listener, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    tweet_stream.filter(track=keywords, languages=languages,
                        locations=locations)
    return tweets_listener.responses


if __name__ == "__main__":
    # test case
    get_tweets(["Python"], ["en"], [-6.38, 49.87, 1.77, 55.81])
