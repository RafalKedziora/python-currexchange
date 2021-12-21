import json
import src.data.currency_api as date_api

def write_currency_data():
    data = date_api.use_currency_api()
    with open('currencies.json', 'w') as file:
        file.write(json.dumps(data))