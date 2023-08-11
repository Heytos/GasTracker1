url = 'https://api.etherscan.io/api'

params = {
    "module": "gastracker",
    "action": "gasoracle",
    "apikey": "FYNDGBGSEY14A1Q2P1APZQ6MMI6V5DCQD6"
}

GAS_PRICE_KEYS = {
    'slow': 'SafeGasPrice',
    'mid': 'ProposeGasPrice',
    'fast': 'FastGasPrice'
}