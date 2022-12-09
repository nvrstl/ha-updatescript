import csv
import time
from requests import post

#DEFINE USER CONSTANTS
update_core_string = "/api/services/update/install"
data = {"entity_id": "update.home_assistant_core_update"}

#OPEN CSV FILE AND SKIP HEADER
with open("server_db.csv", 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader,None)

#ITERATE OVER THE CSV LIST (# of iterations = # of rows)
  for row in csvreader:
    # print(row)
    # print(row[1])
    url = row[2] + update_core_string
    bearer_token = row[1]
    headers = {"Authorization": "{}".format(bearer_token)}
    print(headers)
    print(url)
    print(data)
    print("----------------------------------------")
    response = post(url, headers=headers, json=data)
    print("----------------------------------------")
    print(response.text)
    time.sleep(8)
    
    # print(hassio_url)
    # print(bearer_token)
