import tkinter as tk
from datetime import date

class EmployeeData:
    def __init__(self, szId = '', szName = '', dtmBirthday = date.min):
        self.szId = szId
        self.szName = szName
        self.dtmBirthday = dtmBirthday

    

def win_initialize():
    window = tk.Tk()
    window.geometry("720x360")
    window.title("Main")

    curr_date = tk.Label(window, text=date.today(), font=('Arial Bold', 10))
    curr_date.pack(padx=10, pady=10, anchor='w')

    return window

if __name__ == '__main__':
    window = win_initialize()
    window.mainloop()
