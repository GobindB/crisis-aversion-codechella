from dotenv import load_dotenv
load_dotenv()

import tweepy
import logging
import os

logger = logging.getLogger()

def create_API():
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
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.log("Succesful creation of API.")
    return api