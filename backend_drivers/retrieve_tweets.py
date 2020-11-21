import tweepy
from config import create_api
import time

def follow_followers(api):
    print("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            print(f"Following {follower.name}")
            follower.follow()

def main():
    api = create_api()
    while True:
        follow_followers(api)
        print("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()