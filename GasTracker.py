import requests
import json
import configs
from requests.exceptions import JSONDecodeError

def test():
    print('Ethgdsf')

def gas_tracker():
    response = requests.get(configs.url, params=configs.params)

    if response.status_code != 200:
        return 'Возникла ошибка, попробуйте позднее'

    try:
        data = response.json()
    except JSONDecodeError:
        return "Ошибка при декодировании ответа в формате JSON."

    if 'result' not in data or not isinstance(data['result'], dict):
        return 'Возникла ошибка, переменные не найдены'

    keys = ['SafeGasPrice', 'ProposeGasPrice', 'FastGasPrice']
    for key in keys:
        if key not in data['result']:
            return f'Возникла ошибка {key} не найден'

    slow_gas_price = data['result']['SafeGasPrice']
    mid_gas_price = data['result']['ProposeGasPrice']
    fast_gas_price = data['result']['FastGasPrice']


    return f"Low: {slow_gas_price} gwei\nAvg: {mid_gas_price} gwei\nHigh: {fast_gas_price} gwei"

print(gas_tracker())