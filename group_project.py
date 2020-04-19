import csv

with open("songs.csv") as file:
    csv_reader_object = csv.reader(file)
    for row in csv_reader_object
    print(row)


