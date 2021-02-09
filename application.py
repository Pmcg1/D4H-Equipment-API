import requests
import json
import sys

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


def queryAPI(targetEnding):
    print("\nQuerying API...\n")
    inspectTarget = url+targetEnding

    return dataExtract(inspectTarget)


def introMenuFormat():
    print("\nMain Menu")
    print("---------")
    print("1) View Available Inspection Classes")
    print("2) Select an Inspection")
    print("3) View an Item")
    print("Q) Exit\n")


def menu():
    while True:
        introMenuFormat()
        choice = input("Your Choice: ").lower()

        if choice == "1":
            inspectionsDict = extractInspectionClasses()
            listInspectionClasses(inspectionsDict)
            print("")

        elif choice == "2":
            try:
                inspChoice = input("\nInspection Class ID: ").lower()
                #Return only inspections that have not been completed yet
                targetEnding = "/inspections/"+str(inspChoice)+"/items?completed=false"
                
                response = queryAPI(targetEnding)

                #print(response.status_code)
                print("Contents: ")
                print(json.dumps(response['data'], indent=4))
            except:
                return

        elif choice == "3":
            try:
                itemID = input("\nItem ID: ").lower()
                targetEnding = "/inspections?equipment_id="+str(itemID)

                response = queryAPI(targetEnding)
                #print(response.status_code)
                print("Contents: ")
                print(json.dumps(response['data'], indent=4))

            except:
                return


        elif choice == "q":
            return

        else:
            print("Please try again")


# Extract Inspections from D4H
def extractInspectionClasses(): 
    targetEnding = "/inspections"
    response = queryAPI(targetEnding)
    filename = "inspections"
    printtojson(filename, response)
    responseData = response['data']
    # Create Dict of inspection classes
    inspectionsDict = {}
    i = 1
    for item in responseData:
        i = i+1
        inspectionsDict[item["id"]] = (item["title"])

    return inspectionsDict


def listInspectionClasses(inspectionsDict):
    print("List of inspection classes:")
    for key in inspectionsDict.keys():
        targetEnding = "/inspections/"+str(key)+"/items"
        print("\nItem: ",key, ":", inspectionsDict[key], end =" ")

'''
def retrieveItem(itemID):
    print("Item retrieved:")
    targetEnding = "/equipment/"+itemID
    equipmentTarget = url+targetEnding
    return dataExtract(equipmentTarget)
'''




# Defining variables to access API
base_url = "https://api.d4h.org/v2"
team  = "team"
url = base_url+"/"+team

print("Connecting to: ", url)
print("API Key: ", api_key)

# Check access
print("Welcome to the Inventory Inspector App")
print("Checking Authorisation...")
response = requests.get(url, headers={'Authorization': 'Bearer %s' % api_key})
print("Response from connection check: ",response.status_code)
if (response.status_code == requests.codes.ok):
    print("Good Response")
else:
    print("Not Authorised")


#inspectionsDict = extractInspectionClasses()


#listInspectionClasses(inspectionsDict)

'''
print("List of inspection classes:")
# List contents of each inspection class
for key in inspectionsDict.keys():
    targetEnding = "/inspections/"+str(key)+"/items"
    print("\nItem: ",key, ":", inspectionsDict[key])
    response = queryAPI(targetEnding)
    filename = "inspection-"+str(key)+"-"+str(inspectionsDict[key])
    printtojson(filename, response)
'''

if __name__ == '__main__':
    menu()