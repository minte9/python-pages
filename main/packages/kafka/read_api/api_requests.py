import requests
import json
import time

# API endpoint URL
api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

# Fetch data from the API
while True:
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        print(data, '\n')

    # Fetch data at every 10 seconds
    time.sleep(10)
