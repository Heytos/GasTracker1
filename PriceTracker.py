import requests
import configs_price
from requests.exceptions import HTTPError, JSONDecodeError


def price_check(symbol):

    parameters = {
        'symbol': symbol,
        'convert': 'USD'
    }

    response = requests.get(configs_price.url, params=parameters, headers=configs_price.headers)
    data = response.json()

    try:
        response.raise_for_status()
    except JSONDecodeError:
        return "Ошибка при декодировании ответа в формате JSON."
    except HTTPError:
        print ('Ошибка в получении данных API')
        return None, None
    except ValueError:
        print ('Произошла ошибка, попробуйте позднее')
        return None, None
    except KeyError:
        print ('Произошла ошибка, попробуйте позднее')
        return None, None

    price = data['data'][symbol]["quote"]['USD']['price']
    percent_change_24h = data['data'][symbol]['quote']['USD']['percent_change_24h']

    return price, percent_change_24h


def display_price():
    token_symbol = input("Введите криптовалюту: ").upper()
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



