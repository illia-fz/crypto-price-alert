import requests


def get_price(symbol):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[symbol]['usd']


def main():
    # Define symbols and their alert thresholds in USD
    watch = {
        'bitcoin': 30000,
        'ethereum': 2000
    }
    for symbol, threshold in watch.items():
        price = get_price(symbol)
        if price >= threshold:
            print(f"ALERT: {symbol.capitalize()} price ${price} has reached or exceeded threshold ${threshold}")
        else:
            print(f"{symbol.capitalize()} price ${price} is below threshold ${threshold}")


if __name__ == '__main__':
    main()
