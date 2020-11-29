import requests
import json
from pathlib import Path
from flask import jsonify, make_response

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
print("Response from connection check: ",response.status_code)

'''
# Return list of events
response = requests.get(url+"/events"+"?after=2020-07-01"+"&before=2020-09-30", headers={'Authorization': 'Bearer %s' % api_key})
print("Events GET response: ",response.status_code)

# Print to file
filename = "events"
printtojson(filename, response)

# Return list of exercises
response = requests.get(url+"/exercises"+"?after=2020-07-01"+"&before=2020-09-30", headers={'Authorization': 'Bearer %s' % api_key})
print("Exercises GET response: ",response.status_code)

# Print to file
filename = "exercises"
printtojson(filename, response)

# Return list of incidents
response = requests.get(url+"/incidents"+"?after=2020-07-01"+"&before=2020-09-30", headers={'Authorization': 'Bearer %s' % api_key})
print("Incidents GET response: ",response.status_code)

# Print to file
filename = "incidents"
printtojson(filename, response)
'''

# Return all current attendance records
response = requests.get(url+"/attendance"+"?after=2020-07-01"+"&before=2020-09-30", headers={'Authorization': 'Bearer %s' % api_key})
print("Attendance GET response: ",response.status_code)

# Print to file
filename = "attendance"
printtojson(filename, response)