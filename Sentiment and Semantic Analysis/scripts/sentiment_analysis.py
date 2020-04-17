import json
import re
import csv

def search(list, word):
    for i in range(len(list)):
        print(list[i])
        if str(list[i]) == word:
            return True
    return False

def freq_count(tweet):
    words = tweet.split()
    dict = {}
    for word in words:
        dict[word] = 0
    for word in words:
        dict[word] += 1
    return dict

def sentiment_analysis():
    for idx,tweet in enumerate(data):
        bow_dict = {}
        analysis = {}
        pos = 0
        neg = 0
        name = 'bow' + str(idx + 1)
        bow_dict[name] = freq_count(tweet['text'])
        list_of_bow.append(bow_dict)
        analysis['Tweet'] = idx + 1
        analysis['Message'] = tweet['text']
        list_pos = []
        list_neg = []
        for word in bow_dict[name]:
            if word.casefold() in positive_words:
                pos += 1
                list_pos.append(word)
                master_positive_list.append(word)
            elif word.casefold() in negative_words:
                neg += 1
                list_neg.append(word)
                master_negative_list.append(word)
        if pos > neg:
            analysis['polarity'] = 'positive'
            analysis['match'] = list_pos
        elif neg > pos:
            analysis['polarity'] = 'negative'
            analysis['match'] = list_neg
        else:
            analysis['polarity'] = 'neutral'
        list_table.append(analysis)


filename = '../JSON/tweets.json'
table = '../sentiment_analysis_table.json'
f = open(filename)
positive = open('../TXT/positive-words.txt')
negative = open('../TXT/negative-words.txt')
data = json.load(f)
master_positive_list = []
master_negative_list = []
list_of_bow = []
list_table = []
positive_words = []# = positive.readlines()
negative_words = []# = negative.readlines()

for line in positive.readlines():
    positive_words.append(line[:-1])

for line in negative.readlines():
    negative_words.append(line[:-1])

sentiment_analysis()

with open("../JSON/bag_of_words.json",'w') as out:
    json.dump(list_of_bow, out, indent=4)

with open(table,'w') as out:
    json.dump(list_table, out, indent=4)

file = open('../sentiment_analysis_table.json')
tableObj = json.load(file)
csv_out = open("../sentiment_table.csv" ,'w')
csvwriter = csv.writer(csv_out)

csvwriter.writerow(tableObj[0].keys())
for row in tableObj:
    csvwriter.writerow(row.values())

with open("../TXT/positive_tableau.txt", 'w') as out:
    for word in master_positive_list:
        out.write(word)
        out.write("\n")

with open("../TXT/negative_tableau.txt", 'w') as out:
    for word in master_negative_list:
        out.write(word)
        out.write("\n")
