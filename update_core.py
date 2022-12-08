
from requests import post

url = "http://192.168.0.157:8123/api/services/update/install"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmNDgzZTQzODZmZDc0ODJjYjNkYmJkNWFiZDQ5OGMwOSIsImlhdCI6MTY3MDQ5MzY4OCwiZXhwIjoxOTg1ODUzNjg4fQ.Z8z0n4iL97yVlYLEWEVnwgM473c_8u2uLQINkhLkprE"}
data = {"entity_id": "update.home_assistant_core_update"}

response = post(url, headers=headers, json=data)
print(response.text)