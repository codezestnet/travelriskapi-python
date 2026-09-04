import logging
from typing import Optional
import requests
from classes import Countries

def fetch_countries(api_urlbase: str, api_key: str) -> Optional[Countries]:

    url = f"{api_urlbase}countries?limit=250"

    # Set the headers with the API key
    headers = {"X-API-Key": f"{api_key}"}

    # Make the GET Request to the API
    payload = {}
    try:
        response = requests.request("GET", url, headers=headers, data=payload)

        # Check if the request was successful
        if response.status_code == 200:
    
            known = Countries.__dataclass_fields__
            payload = {k: v for k, v in response.json().items() if k in known}
            return Countries(**payload)
    
        else:
    
            return None

    except requests.RequestException as e:
        logging.error(f"Error fetching country data from the API: {e}")
        return None 

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None

