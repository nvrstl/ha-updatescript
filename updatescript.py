import csv
from requests import post

with open("test_db.csv", 'r') as file:
  csvreader = csv.reader(file)

  
  #Iterate over the csv list (# of rows = # of iterations)
  for row in csvreader:
    print(row[0].split(",")[0])
