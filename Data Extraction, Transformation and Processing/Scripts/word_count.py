from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("Test")
# setMaster(local) - we are doing tasks on a single machine
sc = SparkContext(conf = conf)

# read data from text file and split each line into words
words = sc.textFile("../TXT/input_for_word_count.txt").flatMap(lambda line: line.split(" "))

# count the occurrence of each word
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)

# save the counts to output

list_of_words = ["education", "Canada", "University", "Dalhousie", "expensive", "good school", "good schools", "bad school", "faculty", "Computer Science", "graduate" ]
wordsList = wordCounts.collect()
f = open("../TXT/output.txt", "w")
for word in list_of_words:
    flag = False
    for l in wordsList:
        if word == l[0]:
            print(str(l[0]), l[1])
            f.write("%s %s\n" % (str(l[0]), l[1]))
            flag = True
            break
    if flag == False:
        print(word, 0)
        f.write("%s %s\n"% (word, 0))

print("")
