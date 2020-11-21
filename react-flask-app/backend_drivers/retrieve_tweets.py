import tweepy
import pymysql
import dotenv
import json, string, os, time
from config import create_api
from misinformation_model import calculate_validity_score


class TweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.responses = []
        self.num_tweets = 0
        self.limit = 2
    
    def increment_num_tweets(self):
        self.num_tweets += 1

    def on_status(self, tweet):
        """
        Process the tweets and save them to a PyMySQL AWS database
        """
        print(f"Processing tweet id {tweet.id}\n")
        print(f"Tweet: {tweet.text}\n")
        
        # serve this ID and score to the client
        score = calculate_validity_score(tweet)

        # TODO: extended text
        self.insert_into_database(tweet.created_at, tweet.text, tweet.user.screen_name, tweet.id, score)

        response = {'id': tweet.id, 'handle': tweet.user.screen_name,'created_at': tweet.created_at, 'text': tweet.text}
        self.responses.append(response)

        self.increment_num_tweets()
        if self.num_tweets < self.limit:
                return True
        else:
            return False

    # save to database for data analytics 
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
# this may not work because the filter may not be able to get all together
def get_tweets(keywords, languages, locations):
    api = create_api()
    tweets_listener = TweetListener(api)
    tweets_listener.keywords = keywords
    tweet_stream = tweepy.Stream(api.auth, tweets_listener, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    tweet_stream.filter(track=keywords, languages=languages,locations=locations)
    tweets_listener.increment_num_tweets()

    return tweets_listener.responses

if __name__ == "__main__":
    get_tweets(["Python"], ["en"], [-6.38,49.87,1.77,55.81])