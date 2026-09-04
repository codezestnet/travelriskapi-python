#!/usr/bin/python3

import alerts
from classes import Countries
import countries

api_urlbase = "https://travelriskapi.com/api/v1/"
api_key = "<API Key>"

def get_countries():
    data = countries.fetch_countries(api_urlbase, api_key)

    if data is None:
        print("Failed to fetch country data.")
        return

    print(f"Total Countries: {data.total}")

def get_alerts():
    data = alerts.fetch_alerts(api_urlbase, api_key)

    if data is None:
        print("Failed to fetch alert data.")
        return

    print(f"Total Alerts: {data.total}")

def menu():

    while True:
        operation = input('''
Select operation:
[1] Get Country Data
[2] Get Risk Data
[3] Exit Script

''')
        # Handle user input
        if operation == '1': # Get Country Data
            get_countries()

        elif operation == '2': # Get Risk Data
            get_alerts()

        elif operation == '3': # Exit Script
            print("Exiting script.")
            break

        else:
            print("Invalid choice. Please try again.")

def main():
        # Open the menu for user input
        menu()
      
## Main entry point of the script
if __name__ == "__main__":
    main()

