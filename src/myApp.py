from tkinter import *
from tkinter import messagebox
from random import choice
from helpers.exchangeRateUpdater import exchangeRateLocalUpdater, exchangeRateUpdater
from helpers.exchange_value import Operations
from data.fileReader import check_file_exist

class myApp(object):
    currencies = {}
    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.geometry("250x260")
        self.mainWindow.title("KANTOR WALUT")
        filename = PhotoImage(file = "../images/background.png")
        background_label = Label(self.mainWindow, image = filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.init_random_currencies()
        self.init_ui()

        self.mainWindow.mainloop()
    
    def init_random_currencies(self):
        if(not check_file_exist()):
            exchangeRateUpdater()
        self.currencies = exchangeRateLocalUpdater()
        tempdict = {}
        i = 0
        while i<8:    
            temp = choice(list(self.currencies.keys()))
            if(temp not in tempdict): 
                tempdict[temp] = self.currencies[temp]
                i+=1
        self.currencies = tempdict

    def round_entry_value(self):
        val = str(round(float(self.value_in_pln.get()),2))
        self.value_in_pln.delete(0,END)
        self.value_in_pln.insert(0,val)

    def init_ui(self):
        resultBtn = Button(self.mainWindow, text="Oblicz", command=self.show_results)
        resultBtn.grid(row=1, column=0, sticky=W)

        update_exchange_rateBtn = Button(self.mainWindow, text="Aktualizuj kursy walut", command=exchangeRateUpdater)
        update_exchange_rateBtn.grid(row=1, column=1, sticky=W)

        information = Label(self.mainWindow, text="Kwota w PLN")
        information.grid(row=0, column=0, sticky=W)

        self.value_in_pln = Entry(width=10)
        self.value_in_pln.grid(row=0, column=1, sticky=W)
    
    def generate_output_box(self, i):
        value_box = Entry(width=10)
        value_box.grid(row=i+3, column=1, sticky=W)
        return value_box

    def generate_output_label(self,i, key_list):
        information = Label(self.mainWindow, text=key_list[i])
        information.grid(row=i+3, column=0, sticky=W)

    def outputs_ui(self, results):
        result_info = Label(self.mainWindow, text="Kwota w obcych walutach:")
        result_info.grid(row=2, column=0, sticky=W)
        key_list = list(self.currencies.keys())
        for i in range(len(results)):
            self.generate_output_label(i, key_list)
            self.generate_output_box(i).insert(0,str(round(results[i],2)))

    def catch_input_errors(self):
        if not self.value_in_pln.get().replace('.','',1).isnumeric() or float(self.value_in_pln.get()) <= 0:
            messagebox.showwarning("Warning", "Ta wartość nie ma sensu")
            return True
        if not self.value_in_pln.get():
            messagebox.showinfo("Info", "Musisz wprowadzić jakąś wartość")
            return True

    def show_results(self):
        self.init_random_currencies()
        if(not self.catch_input_errors()):
            self.round_entry_value()
            results = Operations.compute_result(float(self.value_in_pln.get()), self.currencies)
            self.outputs_ui(results)

app = myApp()