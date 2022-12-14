import csv
import time
from requests import post
import requests


#DEFINE USER CONSTANTS
update_addon_string = "api/services/hassio/addon_update"
data = {"addon": "a0d7b954_nodered"}

print ("Script has been started!")
#OPEN CSV FILE AND SKIP HEADER
with open("server_db.csv", 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader,None)

#ITERATE OVER THE CSV LIST (# of iterations = # of rows)
  for row in csvreader:
    # print(row)    
    # print(row[1])
    url = row[2] + update_addon_string
    bearer_token = row[1]
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    # print(headers)
    # print(url)
    # print(data) 
    print("----------------------------------------")
    try:
        response = post(url, headers=headers, json=data)
        response.raise_for_status()
        time.sleep(1)
        print("INF: Updating NODE-RED on server: {}".format(url)+" ...")
        time.sleep(2)
        print("INF: NODE-RED on {}".format(url)+"has been sucessfully updated!")
        time.sleep(4)
        print(response.status_code)
    except requests.exceptions.HTTPError as err:
        print("WAR: NODE-RED on server {} has already been updated".format(url))
        time.sleep(4)
    except requests.exceptions.InvalidSchema as errTimeout:
        print("ERR: Can't reach Server {}".format(url))
        time.sleep(4)

    # print(hassio_url)
    # print(bearer_token)
