import tweepy as tw
import json
import os
import re

api_key = 'QsjE7LBLiw3BlmEaqScfYanuO'
api_key_secret = 'ah2ptOhwrwYoc9epyqgqV6Nwq2FTVEdTm0nn4FQDXzAIXGfWPi'
access_token = '2168983267-EFWnLY7j2NP6cPJ1ptAkF9YxRJmwzVdR5qyaQsX'
access_token_secret = '8yhY0Dkj8c3OkoX0JcaV16a4kHnZvDSD4Rqsm2GzE9u5J'


auth = tw.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)

count = 0
keyword = 'Canada'
list = []
filename = "../JSON/tweets.json"
class MyStreamListener(tw.StreamListener):
    def on_error(self, status_code):
        if status_code == 420:
            print("420")
            return False
    def on_status(self, status):
        parsed_tweet = {}
        global count
        count += 1
        print(count)
        if count == 1200:
            return False

        if hasattr(status, "retweeted_status"):
            try:
                parsed_tweet['text'] = status.retweeted_status.extended_tweet["full_text"]
            except AttributeError:
                parsed_tweet['text'] = status.retweeted_status.text
            else:
                try:
                    parsed_tweet['text'] = status.extended_tweet["full_text"]
                except AttributeError:
                    parsed_tweet['text'] = status.text
        else:
            try:
                parsed_tweet['text'] = status.extended_tweet["full_text"]
            except AttributeError:
                parsed_tweet['text'] = status.text
        parsed_tweet['id'] = status.id
        parsed_tweet['created_at'] = str(status.created_at)
        parsed_tweet['source'] = status.source
        list.append(parsed_tweet)



myStreamListener = MyStreamListener()
myStream = tw.Stream(auth = api.auth, listener=myStreamListener, tweet_mode='extended')

keyword = ["Canada", "University"]
for k in keyword:
    count = 0
    myStream.filter(track=[k])


with open(filename,'a') as out:
    json.dump(list, out, indent=4)
