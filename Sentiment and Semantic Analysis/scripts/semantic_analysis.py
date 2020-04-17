import csv
import json
import re
import os
import math
import csv

count = {}
tf_tdf_table = []
filename = "news_articles.json"
total_documents = 700
#list = clean_articles(filename)
list_of_keywords = ['Canada', 'University', 'Dalhousie University', 'Halifax', 'Business']

def clean(article):
    return ' '.join(re.sub("(@[A-Za-z]+)|([^A-Za-z \t])|(\w+:\/\/\S+)", " ", article).split())

def clean_articles(filename):
    list_of_articles = []
    f = open(filename)
    data = json.load(f)
    for x in data:
        article = {}
        article['title'] = x['title']
        article['description'] = x['description']
        article['content'] = clean(str(x['content']))
        list_of_articles.append(article)

    return list_of_articles

def tf_tdf(list_of_keywords):
    directory = '../newsArticles'
    for word in list_of_keywords:
        dict = {}
        dict['Query'] = word

        doc_count = 0
        for x in os.walk(directory):
            for file in x[2]:
                cnt = 0
                filename = directory + "/" + file
                f = open(filename)
                data = json.load(f)
                content = str(data['content'])
                if re.search(word, content, re.IGNORECASE):
                    doc_count += 1
        dict['Documents_containing_term'] = doc_count
        freq = total_documents / doc_count
        dict['n/df'] = round(freq, 2)
        log = math.log(freq, 10)
        dict['log(n/df)'] = round(log, 2)
        tf_tdf_table.append(dict)

    csv_out = open("../keyword_tf_tdf.csv" ,'w')
    csvwriter = csv.writer(csv_out)
    csvwriter.writerow(tf_tdf_table[0].keys())
    for row in tf_tdf_table:
        csvwriter.writerow(row.values())

def relativeFrequency():
    directory = '../newsArticles'
    max_rf = 0
    max_rf_article = ""
    for word in list_of_keywords:
        list = []

        doc_count = 0
        for x in os.walk(directory):
            for file in x[2]:
                cnt = 0
                filename = directory + "/" + file
                f = open(filename)
                data = json.load(f)
                content = str(data['content'])
                if re.search(word, content, re.IGNORECASE):
                    dict = {}
                    doc_count += 1
                    dict['Article'] = file.split(".")[0]
                    freq = len(re.findall(word, content, re.IGNORECASE))
                    dict['frequency'] = freq
                    total_words =  len(content.split(" "))
                    dict['Total words'] = total_words
                    rf = freq / total_words
                    if rf > max_rf:
                        max_rf = rf
                        max_rf_article = content
                    list.append(dict)

        filename = "../Semantic_analysis_table/" + word + ".csv"
        csv_out = open(filename ,'w')
        csvwriter = csv.writer(csv_out)
        csvwriter.writerow(list[0].keys())
        for row in list:
            csvwriter.writerow(row.values())
    print("Highest Relative Frequency News Articles")
    print(max_rf_article)

tf_tdf(list_of_keywords)
relativeFrequency()
"""
for idx, article in enumerate(list):
    fn = "./newsArticles/article_" + str(idx) + ".json"
    with open(fn,'w') as out:
        json.dump(article, out, indent=4)
"""
