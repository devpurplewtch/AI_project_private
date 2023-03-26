import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set up a list of cryptocurrencies to analyze
cryptos = ['bitcoin', 'ethereum', 'cardano', 'binancecoin', 'dogecoin', 'solana', 'polkadot', 'chainlink', 'ripple', 'litecoin']

# create an empty dictionary to store the data for each cryptocurrency
crypto_data = {}

# loop over the list of cryptocurrencies and retrieve data from the CoinGecko API
for crypto in cryptos:
    # set up the API endpoint URL for the current cryptocurrency
    url = f"https://api.coingecko.com/api/v3/coins/{crypto}"
    
    # use the requests library to send a GET request to the API endpoint
    response = requests.get(url)
    
    # parse the response JSON into a Python dictionary and store it in the crypto_data dictionary
    data = response.json()
    crypto_data[crypto] = data

# create a Pandas DataFrame to store the relevant data for each cryptocurrency
df = pd.DataFrame(columns=['Name', 'Symbol', 'Price (USD)', 'Market Cap (USD)', '24h % Change', '7d % Change', '30d % Change'])

# loop over the crypto_data dictionary and extract the relevant data for each cryptocurrency
for crypto, data in crypto_data.items():
    name = data['name']
    symbol = data['symbol'].upper()
    price = data['market_data']['current_price']['usd']
    market_cap = data['market_data']['market_cap']['usd']
    day_change = data['market_data']['price_change_percentage_24h']
    week_change = data['market_data']['price_change_percentage_7d']
    month_change = data['market_data']['price_change_percentage_30d']
    df = df.append({'Name': name, 'Symbol': symbol, 'Price (USD)': price, 'Market Cap (USD)':
