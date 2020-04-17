import csv;

dictionary = {}
with open('DNR_Camping_Parks_Reservation_Data_2016.csv', 'r') as file1, open('file1.csv', 'w') as file2:
    csv_reader = csv.reader(file1, delimiter=',')
    csv_writer = csv.writer(file2, delimiter=',')
    line_no = 0
    for row in csv_reader:
        if line_no == 0:
            csv_writer.writerow(row)
            for idx, element in enumerate(row):
                dictionary[element] = idx
        else:
            if row[2] == 'CANADA ':
                csv_writer.writerow(row)
        line_no+=1


columns = ['ParkName ', 'State ', 'PartySize ', 'BookingType ', 'RateType ', 'Equipment ']

with open('file1.csv', 'r') as file1, open('file2.csv', 'w') as file2:
    csv_reader = csv.reader(file1, delimiter=',')
    csv_writer = csv.writer(file2, delimiter=',')
    line_no = 0

    for row in csv_reader:
        index = []
        index.append(row[0])
        index.append(row[1])
        index.append(row[5])
        index.append(row[6])
        index.append(row[7])
        index.append(row[8])
        csv_writer.writerow(index)

with open('file2.csv', 'r') as file2, open('file3.csv', 'w') as file3:
    csv_reader = csv.reader(file2, delimiter=',')
    csv_writer = csv.writer(file3, delimiter=',')

    for row in csv_reader:
        list = row[0:4]
        temp = row[5]
        l = temp.split()
        if l[0] == 'Less':
            str = "LT" + l[2]
        elif l[0] == 'Single':
            str = "ST"
        else:
            str = row[5]
        list.append(str)
        csv_writer.writerow(list)


with open('file3.csv', 'r') as file3, open('file4.csv', 'w') as file4:
    csv_reader = csv.reader(file3, delimiter=',')
    csv_writer = csv.writer(file4, delimiter=',')

    line_no = 0
    for row in csv_reader:

        if line_no == 0:
            csv_writer.writerow(row)
        else:
            if row[1] == "NS ":
                csv_writer.writerow(row)
        line_no+=1
