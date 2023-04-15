import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class AgeCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор возраста")

        self.label1 = tk.Label(master, text="Введите дату рождения (**.**.****):")
        self.label1.pack()
        
        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        self.button1 = tk.Button(master, text="Рассчитать возраст", command=self.calculate_age)
        self.button1.pack()

        self.label2 = tk.Label(master, text="")
        self.label2.pack()

    def calculate_age(self):
        date_format = '%d.%m.%Y'
        try:
            birth_date = datetime.strptime(self.entry1.get(), date_format)
        except ValueError:
            messagebox.showerror("Ошибка", "Введите дату в формате **.**.****")
            return

        age_in_days = (datetime.today() - birth_date).days
        self.label2.configure(text=f"Ваш возраст: {age_in_days} дней")

root = tk.Tk()
calculator = AgeCalculator(root)
root.mainloop()
