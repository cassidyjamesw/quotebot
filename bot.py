import tweepy
import time

#from keys import *
from quotes import *

from decouple import config
CONSUMER_KEY = config('CONSUMER_KEY')
CONSUMER_SECRET = config('CONSUMER_SECRET')
ACCESS_KEY = config('ACCESS_KEY')
ACCESS_SECRET = config('ACCESS_SECRET')


print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def quoteMachine():
    for quote in quotelist:
        try:
            api.update_status(quote)
            time.sleep(3600)
        except:
            continue
    quoteMachine()


print("Starting")
quoteMachine()

