import requests
headers={"Authorization": "Bearer 891f4807-05a1-4f0a-b27d-d91a2e5df844"}
response= requests.get("https://vco22-fra1.velocloud.net//api/sdwan/v2", headers=header)
print(response.json)

