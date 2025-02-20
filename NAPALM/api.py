import requests
headers={"Authorization": "Bearer *************"}
response= requests.get("https://vco22-fra1.velocloud.net//api/sdwan/v2", headers=header)
print(response.json)

