import requests
import json
import configs
from requests.exceptions import JSONDecodeError

def gas_tracker():
    response = requests.get(configs.url, params=configs.params)

    try:
        data = response.json()
    except JSONDecodeError:
        return "Ошибка при декодировании ответа в формате JSON."


    slow_gas_price = data['result']['SafeGasPrice']
    mid_gas_price = data['result']['ProposeGasPrice']
    fast_gas_price = data['result']['FastGasPrice']

    if 'result' not in data or not isinstance(data['result'], dict):
        return 'Возникла ошибка, переменные не найдены'

    keys = ['SafeGasPrice', 'ProposeGasPrice', 'FastGasPrice']
    for key in keys:
        if key not in data['result']:
            return f'Возникла ошибка {key} не найден'

    if response.status_code != 200:
        return 'Возникла ошибка, попробуйте позднее'
    else:
        return f"Low: {slow_gas_price} gwei\nAvg: {mid_gas_price} gwei\nHigh: {fast_gas_price} gwei"

print(gas_tracker())