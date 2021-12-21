import json

def read_currency_data():
    f = open('currentExchangeRate.json', 'r')
    data = json.load(f)
    
    for i in data["conversion_rates"]:
        print(i)
    
    f.close()

    return data