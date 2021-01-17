import requests
import json

from pathlib import Path
from flask import jsonify, make_response

from config import api_key


# Function to dump JSON to a file
def printtojson(filename, response):
    # Create outputs directory if it doesn't already exist
    Path('outputs').mkdir(parents=True, exist_ok=True) 
    #print(type(response))

    # Build filepath
    filepath = ('outputs/%s.json' %filename)

    # Dump json to the file
    with open (filepath, 'w') as f:
        json.dump(response, f, indent = 4)
        
def dataExtract(target):
    print("Target: ",target)
    response = requests.get(target, headers={'Authorization': 'Bearer %s' % api_key})
    print("Response: ", response.status_code)
    return response.json()


# Defining variables to access API
base_url = "https://api.d4h.org/v2"
team  = "team"
url = base_url+"/"+team

print("Connecting to: ", url)
print("API Key: ", api_key)

# Check access
response = requests.get(url, headers={'Authorization': 'Bearer %s' % api_key})
print("Response from connection check: ",response.status_code)

def queryAPI(targetEnding):
    inspectTarget = url+targetEnding
    return dataExtract(inspectTarget)

# Extract Inspections
targetEnding = "/inspections"
response = queryAPI(targetEnding)
filename = "inspections"
printtojson(filename, response)


responseData = response['data']


inspectionsDict = {}
#print("Data: ",response['data'])
print("List of inspection classes:")
i = 1
for item in responseData:
    #inspectionTitle = item[2]
    #print("Inspection class",i,":", item["title"])
    i = i+1
    #print(item["id"], ":", item["title"])
    inspectionsDict[item["id"]] = (item["title"])


for key in inspectionsDict.keys():
    #for value in inspectionsDict[key]:
    targetEnding = "/inspections/"+str(key)+"/items"
    print("\nItem: ",key, ":", inspectionsDict[key])
    response = queryAPI(targetEnding)
    filename = "inspection-"+str(key)+"-"+str(inspectionsDict[key])
    printtojson(filename, response)
