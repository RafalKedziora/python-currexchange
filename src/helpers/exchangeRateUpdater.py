from data import currency_api
import data.fileWriter as file_writer
import data.fileReader as file_reader

def exchangeRateUpdater():
     file_writer.write_currency_data(currency_api.use_currency_api())

def exchangeRateLocalUpdater():
    data = file_reader.read_currency_data()
    return data