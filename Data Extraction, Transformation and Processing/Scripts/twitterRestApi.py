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

list = []
filename = "../JSON/tweets.json"
arr = ['Dalhousie University', 'Halifax', 'Canada Education']

for keyword in arr:
    tweets = api.search(q=keyword, lang='en', count = 100, tweet_mode='extended')
    for tweet in tweets:
        parsed_tweet = {}
        parsed_tweet['id'] = tweet.id
        parsed_tweet['source'] = tweet.source
        parsed_tweet['text'] = tweet.full_text
        parsed_tweet['created_at'] = str(tweet.created_at)
        list.append(parsed_tweet)

print(list)
with open(filename, "w") as out:
    json.dump(list, out, indent=4)
