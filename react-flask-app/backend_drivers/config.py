from logging import log
from dotenv import load_dotenv
import logging

load_dotenv()

import tweepy
import os

def create_api():
    CONSUMER_KEY = os.getenv("API_key")
    CONSUMER_SECRET = os.getenv("API_key_secret")
    ACCESS_TOKEN = os.getenv("access_token")
    ACCESS_TOKEN_SECRET = os.getenv("access_token_secret")

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logging.error("Error creating API")
        raise e
    logging.info("Succesful creation of API.")
    return api
