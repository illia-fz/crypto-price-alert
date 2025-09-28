import requests
import json
import os


def get_price(symbol):
    """
    Fetch the current USD price for a given cryptocurrency symbol using CoinGecko API.
    """
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[symbol]['usd']


def load_config():
    """
    Load alert thresholds from a local JSON configuration file. If the file does not exist,
    return a default configuration. This allows users to customize which cryptocurrencies to
    monitor and their alert thresholds without modifying the script.
    """
    config_file = 'config.json'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    # Default configuration if no config file is found
    return {
        'bitcoin': 30000,
        'ethereum': 2000,
        'dogecoin': 0.1
    }


def main():
    # Load the watchlist from config
    watchlist = load_config()
    for symbol, threshold in watchlist.items():
        price = get_price(symbol)
        if price >= threshold:
            print(f"ALERT: {symbol.capitalize()} price ${price} has reached or exceeded threshold ${threshold}")
        else:
            print(f"{symbol.capitalize()} price ${price} is below threshold ${threshold}")


if __name__ == '__main__':
    main()
