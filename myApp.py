from tkinter import *
from tkinter import messagebox

currencies = {
    "EURO" : 4.6,
    "USD" : 4.1,
    "GBP" : 5.3,
    "test" : 2.3,
    "ez" : 6.5,
    "ssman" : 9.5,
    "elooo" : 6.5,
    "ostatni" : 5.5
}

class Operations(object):
    @staticmethod
    def compute_result(value):
        result_currencies = []
        for key in currencies:
            result_currencies.append(value/currencies[key])
        return result_currencies

class myApp(object):
    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.geometry("250x260")
        self.mainWindow.title("KANTOR WALUT")
        filename = PhotoImage(file = "background.png")
        background_label = Label(self.mainWindow, image = filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.init_ui()

        self.mainWindow.mainloop()

    def init_ui(self):
        resultBtn = Button(self.mainWindow, text="Oblicz", command=self.show_results)
        resultBtn.grid(row=1, column=0, sticky=W)

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

    def round_entry_value(self):
        val = str(round(float(self.value_in_pln.get()),2))
        self.value_in_pln.delete(0,END)
        self.value_in_pln.insert(0,val)

    def outputs_ui(self, results):
        result_info = Label(self.mainWindow, text="Kwota w obcych walutach:")
        result_info.grid(row=2, column=0, sticky=W)
        key_list = list(currencies.keys())
        for i in range(len(results)):
            self.generate_output_label(i, key_list)
            self.generate_output_box(i).insert(0,str(round(results[i],2)))

    def catch_input_errors(self):
        if not self.value_in_pln.get().isnumeric() or float(self.value_in_pln.get()) <= 0:
            messagebox.showwarning("Warning", "Ta wartość nie ma sensu")
            return True
        if not self.value_in_pln.get():
            messagebox.showinfo("Info", "Musisz wprowadzić jakąś wartość")
            return True

    def show_results(self):
        if(not self.catch_input_errors()):
            self.round_entry_value()
            results = Operations.compute_result(float(self.value_in_pln.get()))
            self.outputs_ui(results)


app = myApp()