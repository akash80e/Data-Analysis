
import csv
with open('file4.csv', 'r') as file4:
    csv_reader = csv.reader(file4, delimiter=',')

    line_no = 0
    dict = {}
    for row in csv_reader:
        if line_no != 0:
            PartySize = int(row[2])
            if row[0] in dict:
                if PartySize > dict[row[0]]:
                    dict[row[0]] = PartySize
            else:
                dict[row[0]] = PartySize
        line_no+=1

print(dict)

with open('file4.csv', 'r') as file4, open('file5.csv', 'w') as file5:
    csv_reader = csv.reader(file4, delimiter=',')
    csv_writer = csv.writer(file5, delimiter=',')
    line_no = 0
    dict2 = {}
    for row in csv_reader:
        if line_no == 0:
            csv_writer.writerow(row)
        else:
            PartySize = int(row[2])
            if PartySize == dict[row[0]] and row[0] not in dict2:
                csv_writer.writerow(row)
                dict2[row[0]] = PartySize
        line_no+=1
