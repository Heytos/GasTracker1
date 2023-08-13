import requests
from requests.exceptions import HTTPError

def price_check(symbol):
    # url вынести в конфиг (как и параметры и заголовки)
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        'symbol': symbol,
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'YOUR_API_KEY',
    }

    response = requests.get(url, params=parameters, headers=headers)

    # может вылететь JSONDecodeError
    data = response.json()

    #  https://stackoverflow.com/questions/61463224/when-to-use-raise-for-status-vs-status-code-testing
    try:
        response.raise_for_status()
        price = data['data'][symbol]["quote"]['USD']['price']
        percent_change_24h = data['data'][symbol]['quote']['USD']['percent_change_24h']
    except HTTPError:
        print ('Ошибка в получении данных API')
        return None, None
    except ValueError:
        print ('Произошла ошибка, попробуйте позднее')
        return None, None
    except KeyError:
        print ('Произошла ошибка, попробуйте позднее')
        return None, None

    # Дублируешь получение цены, сначала в трай, потому тут
    price = data['data'][symbol]["quote"]['USD']['price']
    percent_change_24h = data['data'][symbol]['quote']['USD']['percent_change_24h']

    return price, percent_change_24h

# надо в display_price() засунуть
token_symbol = input("Введите криптовалюту: ").upper()

# if __name__ == "__main__":
def display_price():
    price, percent_change_24h = price_check(token_symbol)

    if price is None or percent_change_24h is None:
        print("Не удалось получить данные для", token_symbol)
    else:
        print(f'Цена {token_symbol} {price:.2f} $')
        if percent_change_24h > 0:
            print(f'+{percent_change_24h:.2f}%')
        else:
            print(f' {percent_change_24h:.2f}%')

if __name__ == "__main__":
    display_price()



