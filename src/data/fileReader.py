import json
from pathlib import Path

path = '../json_files/currentExchangeRate.json'

def check_file_exist():
    f = Path(path)
    if f.exists():
        return True
    return False

def read_currency_data():
    f = open(path, 'r')
    data = json.load(f)
    f.close()

    return data["conversion_rates"]