from tkinter import messagebox
import requests

def use_currency_api():
    url = 'TUTAJ WPISZ SWOJE API OD https://www.exchangerate-api.com/'
    try:
        response = requests.get(url)
        data = response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Błędne połączenie API")
    return data
