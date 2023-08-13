import requests
import json
import configs
from requests.exceptions import JSONDecodeError
from requests.exceptions import HTTPError
from configs import GAS_PRICE_KEYS

def display_gas():
    response = requests.get(configs.url, params=configs.params)

    try:
        response.raise_for_status()
        data = response.json()
    except JSONDecodeError:
        return "Ошибка при декодировании ответа в формате JSON."
    except HTTPError:
        return ('Ошибка в получении данных API')

    if 'result' not in data or not isinstance(data['result'], dict):
        return 'Возникла ошибка, переменные не найдены'

    for key in GAS_PRICE_KEYS:
        if key not in GAS_PRICE_KEYS:
            return f'Возникла ошибка {key} не найден'

    slow_gas_price = data['result'][GAS_PRICE_KEYS['slow']]
    mid_gas_price = data['result'][GAS_PRICE_KEYS['mid']]
    fast_gas_price = data['result'][GAS_PRICE_KEYS['fast']]

    return (f"\nLow: {slow_gas_price} gwei\nAvg: {mid_gas_price} gwei\nHigh: {fast_gas_price} gwei")

