import requests
import json
#import os
#import errno
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

def printtojson(filename, response):
    #dir_path = Path("outputs")
    Path('outputs').mkdir(parents=True, exist_ok=True) 
    filepath = ('/outputs/%s.json' %filename)
    print("Output filepath: ", filepath)
    #os.makedirs(os.path.dirname(filepath), exist_ok=True)
    #pathlib.Path('/outputs').mkdir(parents=True, exist_ok=True) 
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

# Extract equipment
response = requests.get(url+"/equipment", headers={'Authorization': 'Bearer %s' % api_key})
print("Equipment GET response: ",response.status_code)


# Print to file
filename = "equipment"
printtojson(filename, response)