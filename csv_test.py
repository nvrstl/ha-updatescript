import csv

with open("biostats.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)
