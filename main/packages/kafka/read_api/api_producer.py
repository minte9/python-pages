from kafka import KafkaProducer
import requests
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# API endpoint URL
api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

# Fetch data from the API
while True:
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        message = json.dumps(data)
        producer.send('ApiDataTopic', value=message.encode())
        print('Produced:', message)

        time.sleep(30)

"""
    Produced: {"time": {"updated": "Nov 18, 2023 17:29:00 UTC", 
    "updatedISO": "2023-11-18T17:29:00+00:00", "updateduk": "Nov 18, 2023 at 17:29 GMT"}, 
    "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). 
    Non-USD currency data converted using hourly conversion rate from openexchangerates.org", 
    "chartName": "Bitcoin", "bpi": {
    "USD": {"code": "USD", "symbol": "&#36;", "rate": "36,680.0738", 
    "description": "United States Dollar", "rate_float": 36680.0738}, 
    "GBP": {"code": "GBP", "symbol": "&pound;", "rate": "30,649.5762", 
    "description": "British Pound Sterling", "rate_float": 30649.5762}, 
    "EUR": {"code": "EUR", "symbol": "&euro;", "rate": "35,731.7472", 
    "description": "Euro", "rate_float": 35731.7472}}}
    ...
"""