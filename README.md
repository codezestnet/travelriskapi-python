# Travel Risk API - Python Scripts

Python API consumer scripts to capture JSON data from [https://travelriskapi.com](https://travelriskapi.com/)

## Python Requirements

* logging
* requests
* typing
* dataclasses

## Install Requirements

Install Python 3 and PIP then use the commands based on your installation.

`pip install logging`

`pip install requests`

`pip install typing`

`pip install dataclasses`

## Usage

Use demo key from [this page](https://travelriskapi.com/#get-started) or register to obtain free API Key

### Get Country Data

Replace `<API Key>` in countries.py line 9 with your API Key or DEMO key

On cmd line run `python ./countries.py` *depends on local python install*

### Get Alerts Data

Replace `<API Key>` in alerts.py line 9 with your API Key or DEMO key

On cmd line run `python ./alerts.py` *depends on local python install*
