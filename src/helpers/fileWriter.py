import json

def write_currency_data(data):
    with open('./json_files/currentExchangeRate.json', 'w') as file:
        file.write(json.dumps(data, indent=8))