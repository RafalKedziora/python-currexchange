import json
from pathlib import Path

def check_file_exist():
    f = Path('./json_files/currentExchangeRate.json')
    if f.is_file():
        return True
    return False

def read_currency_data():
    f = open('./json_files/currentExchangeRate.json', 'r')
    data = json.load(f)
    f.close()

    return data["conversion_rates"]