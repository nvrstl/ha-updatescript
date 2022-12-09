import csv
from requests import post

with open("test_db.csv", 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader,None)
  
  #Iterate over the csv list (# of rows = # of iterations)
  for row in csvreader:
    print(row)
    print(row[1])

    hassio_url = row[2]
    bearer_token = row[1]
    print(hassio_url)
    print(bearer_token)
