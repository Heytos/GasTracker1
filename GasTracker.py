import requests
import json
import GasTracker_configs
from requests.exceptions import JSONDecodeError
from requests.exceptions import HTTPError
from GasTracker_configs import GAS_PRICE_KEYS

def gas_tracker():
    response = requests.get(GasTracker_configs.url, params=GasTracker_configs.params)

    try:
        response.raise_for_status()
        data = response.json()
    except JSONDecodeError:
        return "Ошибка при декодировании ответа в формате JSON."
    except HTTPError:
        return ('Ошибка в получении данных API')

    if 'result' not in data or not isinstance(data['result'], dict):
        return 'Возникла ошибка, переменные не найдены. Проверьте ваш API'

    for key in GAS_PRICE_KEYS:
        if key not in GAS_PRICE_KEYS:
            return f'Возникла ошибка {key} не найден'

    slow_gas_price = data['result'][GAS_PRICE_KEYS['slow']]
    mid_gas_price = data['result'][GAS_PRICE_KEYS['mid']]
    fast_gas_price = data['result'][GAS_PRICE_KEYS['fast']]

    return f"Low: {slow_gas_price} gwei\nAvg: {mid_gas_price} gwei\nHigh: {fast_gas_price} gwei"

print(gas_tracker())