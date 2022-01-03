import json
import os

path = '../json_files/'

def write_currency_data(data):
    if(not os.path.exists(path)):
        os.makedirs(path)
    with open(path+'currentExchangeRate.json', 'w') as file:
        file.write(json.dumps(data, indent=8))