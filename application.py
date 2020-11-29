import requests
import json

def jsonformat(obj):
    response = json.dumps(obj, indent=2)
    print(response)


from config import api_key

base_url = "https://api.d4h.org/v2"
team  = "team"
url = base_url+"/"+team


print("Connecting to: ", url)
print("API Key: ", api_key)

response = requests.get(url, headers={'Authorization': 'Bearer %s' % api_key})
print(response.status_code)
print(response.iter_lines())

response = requests.get(url+"/equipment", headers={'Authorization': 'Bearer %s' % api_key})
print(response.status_code)
print(response.iter_lines())

jsonformat(response.json())
#print(response)