#!/usr/bin/python3

import logging
import requests

from classes import Countries

api_urlbase = "https://travelriskapi.com/api/v1/"
api_key = "<PASTE API CODE HERE>"

url = f"{api_urlbase}countries?limit=250"

# Set the headers with the API key
headers = {"X-API-Key": f"{api_key}"}

# Make the GET Request to the API
payload = {}
response = requests.request("GET", url, headers=headers, data=payload)

# Check if the request was successful
if response.status_code == 200:
    logging.info("Successfully fetched country data from the API.")

    countries = Countries(**response.json())

    print(f"Countries Data: {countries}") 
else:
    logging.error("Failed to fetch country data from the API.") 
