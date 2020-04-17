import requests
import json
import os
import re
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["movies"]
mycol = mydb["titles"]

arr = ['Canada', 'University', 'Halifax','Moncton', 'Toronto', 'Vancouver', 'Alberta', 'Niagara']
list = []
def clean(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

list = []
list_to_clean = ['Director', 'Writer', 'Plot', 'Actors']
for keyword in arr:
    dict = {}
    url = "http://www.omdbapi.com/?t=" + keyword + "&i=tt3896198&apikey=dec433ca&page=100"
    response = requests.get(url)
    loaded_json = response.json()
    for key in loaded_json:
        if key in list_to_clean:
            dict[key] = clean(loaded_json[key])
        else:
            dict[key] = loaded_json[key]
    list.append(dict)


#mycol.insert_many(list)

filename = "../JSON/movies.json"


with open(filename,'w') as out:
    json.dump(list, out, indent=4)
