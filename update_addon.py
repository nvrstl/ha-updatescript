# from requests import get

# url = "http://debugcontroller.homate.ml/api/services/hassio.addon_update"
# headers = {
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2NjcwMDJiNTI0ZDA0ZjY5OTFkZDk2NTQ5YTlkYjVlZiIsImlhdCI6MTY3MDQyMDI5MCwiZXhwIjoxOTg1NzgwMjkwfQ.ERTpyFAomtsTxjc1ngC0swEEBigPQWvzyFJORetphqw",
#     "content-type": "application/json",
# }

# response = get(url, headers=headers)
# print(response.text)


from requests import post

url = "https://autreve-m1xh9v.homate.ml/api/services/hassio/addon_update"
headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmN2M1ZTIxZDJkMGQ0Y2VjYTNjZjEyNWFmOTBhMDI1ZCIsImlhdCI6MTY3MDU5MzUzMSwiZXhwIjoxOTg1OTUzNTMxfQ.l0aj70FaqdSAi1VWyUIDGLLc1VnLcuzNy__MmbjYKrY"}
data = {"addon": "9074a9fa_cloudflared"}

response = post(url, headers=headers, json=data)
response.raise_for_status()
print(response.status_code)