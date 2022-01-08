from src.data import currency_api
import src.data.fileWriter as file_writer
import src.data.fileReader as file_reader

def exchangeRateUpdater():
     file_writer.write_currency_data(currency_api.use_currency_api())

def exchangeRateLocalUpdater():
    data = file_reader.read_currency_data()
    return data