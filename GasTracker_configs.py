url = 'https://api.etherscan.io/api'

params = {
    "module": "gastracker",
    "action": "gasoracle",
    "apikey": "YOUR_API_TOKEN"
}

GAS_PRICE_KEYS = {
    'slow': 'SafeGasPrice',
    'mid': 'ProposeGasPrice',
    'fast': 'FastGasPrice'
}