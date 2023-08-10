import requests

def get_token_price(symbol):

    symbol = symbol.upper()
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        'symbol': symbol,
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'df269fa7-d67c-463d-88fc-b3c4e2c617bc',
    }

    response = requests.get(url, params=parameters, headers=headers)
    response.raise_for_status()

    data = response.json()
    price = data['data'][symbol]['quote']['USD']['price']
    percent_change_24h = data['data'][symbol]['quote']['USD']['percent_change_24h']

    return price, percent_change_24h


if __name__ == "__main__":
    token_symbol = input(
        "Enter the symbol of the token (e.g. BTC, ETH): ").upper()
    try:
        price, percent_change = get_token_price(token_symbol)
        print(f"\n{token_symbol} is: ${price:.2f}")
        if percent_change > 0:
            print(f"+{percent_change:.2f}% in the last 24 hours.")
        else:
            print(f"-{-percent_change:.2f}% in the last 24 hours.")
    except Exception as e:
        print(f"\nError getting the price for {token_symbol}: {e}")
