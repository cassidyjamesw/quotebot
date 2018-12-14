import tweepy
import time

from keys import *
from quotes import *

print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
print(quotelist)


def quoteMachine():
    for quote in quotelist:
        api.update_status(quote)
        time.sleep(3600)
        quoteMachine()


print("starting again")
quoteMachine()
