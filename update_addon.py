# from requests import get

# url = "http://debugcontroller.homate.ml/api/services/hassio.addon_update"
# headers = {
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2NjcwMDJiNTI0ZDA0ZjY5OTFkZDk2NTQ5YTlkYjVlZiIsImlhdCI6MTY3MDQyMDI5MCwiZXhwIjoxOTg1NzgwMjkwfQ.ERTpyFAomtsTxjc1ngC0swEEBigPQWvzyFJORetphqw",
#     "content-type": "application/json",
# }

# response = get(url, headers=headers)
# print(response.text)


from requests import post

url = "http://debugcontroller.homate.ml/api/services/hassio/addon_update"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2NjcwMDJiNTI0ZDA0ZjY5OTFkZDk2NTQ5YTlkYjVlZiIsImlhdCI6MTY3MDQyMDI5MCwiZXhwIjoxOTg1NzgwMjkwfQ.ERTpyFAomtsTxjc1ngC0swEEBigPQWvzyFJORetphqw"}
data = {"addon": "45df7312_zigbee2mqtt"}

response = post(url, headers=headers, json=data)
print(response.text)