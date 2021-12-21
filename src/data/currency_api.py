import requests

def use_currency_api():
    url = 'https://v6.exchangerate-api.com/v6/815ad457ddcb690f55479f06/latest/PLN'
    response = requests.get(url)
    data = response.json()
    return data