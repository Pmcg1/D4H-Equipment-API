import requests
import json

from pathlib import Path
from flask import jsonify, make_response


#def jsonformat(obj):
#    response = json.dumps(obj, indent=2)
#    print(response)

'''
def printtojson(filename, response):
    with open ('outputs/%s.json' % filename, 'w') as f:
        json.dump(response.json(), f, indent = 4)
'''      

# Function to dump JSON to a file
def printtojson(filename, response):
    # Create outputs directory if it doesn't already exist
    Path('outputs').mkdir(parents=True, exist_ok=True) 


    # Build filepath
    filepath = ('outputs/%s.json' %filename)


    # Dump json to the file
    with open (filepath, 'w') as f:
        json.dump(response.json(), f, indent = 4)




from config import api_key

base_url = "https://api.d4h.org/v2"
team  = "team"
url = base_url+"/"+team


print("Connecting to: ", url)
print("API Key: ", api_key)

# Check access
response = requests.get(url, headers={'Authorization': 'Bearer %s' % api_key})
print("response from connection check: ",response.status_code)

# Extract equipment
response = requests.get(url+"/equipment"+"?limit=3", headers={'Authorization': 'Bearer %s' % api_key})
print("equipment GET response: ",response.status_code)

# Print to file
filename = "equipment"
printtojson(filename, response)

#json_data = json.loads(response.text)
#print("JSON DATA= ",json_data['data'])

#print("response= ", response["data]"].json)
#parsed = json.loads(response["data"])
#print(json.dumps(parsed, indent=4, sort_keys=True))

# Extract inspection resources 
# These are the types of item to inspect
response = requests.get(url+"/inspections", headers={'Authorization': 'Bearer %s' % api_key})
print("inspections GET response: ",response.status_code)

# Print to file
filename = "inspections"
printtojson(filename, response)


# Extract inspections within a resource 
# These are the individual items to inspect (harnesses in this case)
response = requests.get(url+"/inspections/694/items", headers={'Authorization': 'Bearer %s' % api_key})
print("inspection-items GET response: ",response.status_code)

# Print to file
filename = "inspection-items"
printtojson(filename, response)