import re
import json


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tweets"]
mycol = mydb["tweet"]

filename = "tweets.json"

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

f = open(filename)

data = json.load(f)

f = open("../TXT/input_for_word_count.txt", "w")

for x in data:
    text = clean_tweet(x['text'])
    x['text'] = text
    f.write(text)
    f.write(" ")

mycol.insert_many(data)
