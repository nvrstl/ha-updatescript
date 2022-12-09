import csv
import time
from requests import post
import requests


#DEFINE USER CONSTANTS
update_core_string = "/api/services/update/install"
data = {"entity_id": "update.home_assistant_core_update"}
i = 0 

print ("Script has been started!")
#OPEN CSV FILE AND SKIP HEADER
with open("server_db.csv", 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader,None)

#ITERATE OVER THE CSV LIST (# of iterations = # of rows)
  for row in csvreader:
    i = i+1
    # print(row)
    # print(row[1])
    url = row[2] + update_core_string
    bearer_token = row[1]
    headers = {"Authorization": "{}".format(bearer_token)}
    # print(headers)
    # print(url)
    # print(data) 
    print("----------------------------------------")
    try:
        response = post(url, headers=headers, json=data)
        response.raise_for_status()
        print("Updating server: {}".format(url)+"...")
        time.sleep(2)
        print("Server {}".format(url)+"has been sucessfully updated!")
        time.sleep(4)
    except requests.exceptions.HTTPError as err:
        print("ERR: Server {} has already been updated".format(url))
        time.sleep(4)
    # print(hassio_url)
    # print(bearer_token)
