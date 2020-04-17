import json

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["movies"]
mycol = mydb["titles"]

result = mycol.find()
for movie in result:
    print("Title : " + movie['Title'])
    print("Rating :")
    for rating in movie['Ratings']:
        print("%s  %s" % (rating["Source"], rating["Value"]))
    print("Genre : " + movie["Genre"])
    print("Plot : " + movie["Plot"])
    print("")
