#!/usr/bin/python3

import logging
import requests

from classes import Alerts

api_urlbase = "https://travelriskapi.com/api/v1/"
api_key = "<PASTE API CODE HERE>"

url = f"{api_urlbase}alerts?limit=250"

# Set the headers with the API key 
headers = {"X-API-Key": f"{api_key}"}   

# Make the GET Request to the API
payload = {}
response = requests.request("GET", url, headers=headers, data=payload)

# Check if the request was successful
if response.status_code == 200:
    logging.info("Successfully fetched alert data from the API.")

    alerts = Alerts(**response.json())

    print(f"Alert Data: {alerts}") 
else:
    logging.error("Failed to fetch alert data from the API.") 



