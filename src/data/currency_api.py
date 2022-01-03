from tkinter import messagebox
import requests

def use_currency_api():
    url = 'https://v6.exchangerate-api.com/v6/815ad457ddcb690f55479f06/latest/PLN'
    try:
        response = requests.get(url)
        data = response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Błędne połączenie API")
    return data