import json

def read_currency_data():
    f = open('./json_files/currentExchangeRate.json', 'r')
    data = json.load(f)
    f.close()

    return data["conversion_rates"]