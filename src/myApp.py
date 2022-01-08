from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from helpers.exchangeRateUpdater import exchangeRateLocalUpdater, exchangeRateUpdater
from helpers.exchange_value import Operations
from data.fileReader import check_file_exist


class myApp(object):
    currencies = {}

    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.geometry("330x260")
        self.mainWindow.title("KANTOR WALUT")
        filename = PhotoImage(file="../images/background.png")
        background_label = Label(self.mainWindow, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.listOfResults1 = []
        self.listOfResults2 = []

        self.init_chose_currencies()
        self.init_ui()
        self.mainWindow.mainloop()

    def init_chose_currencies(
            self):  # wrzuciłbym to do init_ui chyba że chcemy by to było podzielone bo jest to nieco wieksze
        if (not check_file_exist()):
            exchangeRateUpdater()
        self.currencies = exchangeRateLocalUpdater()
        options = list(self.currencies.keys())
        listOfCurrencies = Listbox(self.mainWindow, height=5, width=10)
        listOfCurrencies.grid(row=2, column=0, sticky=W)
        scrollbar1 = ttk.Scrollbar(self.mainWindow, orient='vertical', command=listOfCurrencies.yview)
        scrollbar1.grid(row=2, column=0, sticky='ns')

        self.listOfChosenC = Listbox(self.mainWindow, height=5, width=10)
        self.listOfChosenC.grid(row=2, column=1, sticky=W)
        scrollbar2 = ttk.Scrollbar(self.mainWindow, orient='vertical', command=self.listOfChosenC.yview)
        scrollbar2.grid(row=2, column=1, sticky='ns')

        for c in range(1, len(options)):
            listOfCurrencies.insert(END, options[c])

        def add():
            newitem = listOfCurrencies.get(ANCHOR)
            if(newitem==''):
                pass
            else:
                added = False
                lis = self.listOfChosenC.get(0, END)
                lis = list(lis)
                for item in lis:
                    if (newitem == item):
                        messagebox.showwarning("Warning", "Ta waluta jest już dodana")
                        added = True
                        break
                if (not added):
                    self.listOfChosenC.insert(END, newitem)

        def delete():
            self.listOfChosenC.delete(ANCHOR)

        def clear():
            self.listOfChosenC.delete(0, END)

        mybutton1 = Button(self.mainWindow, text="dodaj", width=7, command=add)
        mybutton1.grid(row=2, column=3, sticky=NW)
        mybutton2 = Button(self.mainWindow, text="usuń", width=7, command=delete)
        mybutton2.grid(row=2, column=3, sticky=W)
        mybutton3 = Button(self.mainWindow, text="wyczyść", width=7, command=clear)
        mybutton3.grid(row=2, column=3, sticky=SW)

    def round_entry_value(self):
        val = str(round(float(self.value_in_pln.get()), 2))
        self.value_in_pln.delete(0, END)
        self.value_in_pln.insert(0, val)

    def init_ui(self):
        resultBtn = Button(self.mainWindow, text="Oblicz", command=self.show_results)
        resultBtn.grid(row=1, column=0, sticky=W)

        update_exchange_rateBtn = Button(self.mainWindow, text="Aktualizuj kursy walut", command=exchangeRateUpdater)
        update_exchange_rateBtn.grid(row=1, column=1, sticky=W)

        information = Label(self.mainWindow, text="Kwota w PLN")
        information.grid(row=0, column=0, sticky=W)

        self.value_in_pln = Entry(width=10)
        self.value_in_pln.grid(row=0, column=1, sticky=W)

        result_info = Label(self.mainWindow, text="Kwota w obcych walutach:")
        result_info.grid(row=3, column=0, sticky=W)

    def generate_output_box(self, i):
        value_box = Entry(width=10)
        value_box.grid(row=i + 4, column=1, sticky=W)
        self.listOfResults2.append(value_box)
        return value_box

    def generate_output_label(self, i, key_list):
        information = Label(self.mainWindow, text=key_list[i], width=5, anchor=W)
        information.grid(row=i + 4, column=0, sticky=W)
        self.listOfResults1.append(information)

    def outputs_ui(self, results):
        key_list = list(self.currencies.keys())
        for i in range(len(results)):
            self.generate_output_label(i, key_list)
            self.generate_output_box(i).insert(0, str(round(results[i], 2)))

    def catch_input_errors(self):
        if not self.value_in_pln.get().replace('.', '', 1).isnumeric() or float(self.value_in_pln.get()) <= 0:
            messagebox.showwarning("Warning", "Ta wartość nie ma sensu")
            return True
        if not self.value_in_pln.get():
            messagebox.showinfo("Info", "Musisz wprowadzić jakąś wartość")
            return True

    def show_results(self):
        i = len(self.listOfResults1)
        for j in range(0, i):
            self.listOfResults1[i - 1 - j].destroy()
            self.listOfResults2[i - 1 - j].destroy()
        self.listOfResults1.clear()
        self.listOfResults2.clear()
        tmp = self.currencies
        tempdict = {}
        for item in self.listOfChosenC.get(0, END):
            tempdict[item] = self.currencies[item]
        self.currencies = tempdict
        if (not self.catch_input_errors()):
            self.round_entry_value()
            results = Operations.compute_result(float(self.value_in_pln.get()), self.currencies)
            self.outputs_ui(results)
        self.currencies = tmp


if __name__ == "__main__":
    app = myApp()
