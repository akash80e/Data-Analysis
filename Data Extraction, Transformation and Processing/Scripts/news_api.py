import requests
import json
import os
import re


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["news"]
mycol = mydb["articles"]


def clean_articles(news):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", news).split())


arr = ['Canada', 'University', 'Dalhousie', 'Halifax', 'Canada Education', 'Moncton', 'Toronto']

list = []
f = open("../TXT/input_for_word_count.txt", "a")
for keyword in arr:

    loaded_json = {}
    url = "http://newsapi.org/v2/everything?q=" + keyword + "&pageSize=100&apiKey=f9ad4376db3b4d92ad1a4269455d3631"
    response = requests.get(url)
    loaded_json = response.json()

    l = loaded_json['articles']
    for x in l:
        dict = {}
        dict['source'] = x['source']
        dict['author'] = x['author']
        dict['title'] = clean_articles(str(x['title']))
        content = clean_articles(str(x['content']))
        dict['content'] = content
        f.write(content)
        f.write(" ")
        list.append(dict)

mycol.insert_many(list)


#with open("news_articles.json",'w') as out:
#    json.dump(list, out, indent=4)
