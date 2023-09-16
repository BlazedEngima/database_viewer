import tkinter as tk
from datetime import date

rows, cols = 5, 5

class MainForm:
    def __init__(self, employeeList = [], uiList = [None] * 5):
        self.dtmToday = date.today()
        self.employeeList = employeeList
        self.uiList = uiList
    
    def add_employee(self, employeeData):
        self.employeeList.append(employeeData)

    def add_ui(self, uiElement):
        self.uiList.append(uiElement)

    def remove_ui(self, index):
        self.uiList[index] = None

    def display(self):
        print(self.employeeList)
        print(self.uiList)

class EmployeeData:
    def __init__(self, szId = '', szName = '', dtmBirthday = date.min):
        self.szId = szId
        self.szName = szName
        self.dtmBirthday = dtmBirthday
    
class UIData:
    def __init__(self, lblNo='', lblId = '', lblName ='', lblBirthday = '', lblAge = ''):
        self.lblNo = lblNo
        self.lblId = lblId
        self.lblName = lblName
        self.lblBirthday = lblBirthday
        self.lblAge = lblAge

def win_initialize(window):
    window.geometry("840x360")
    window.title("Main")

    curr_date = tk.Label(window, text=date.today(), font=('Arial Bold', 10))
    curr_date.pack(padx=10, pady=10, anchor='w')

def initialize_ui(window):
    headers = ['NO', 'ID', 'NAME', 'BIRTHDAY', 'AGE']
    width = [10, 15, 25, 20, 30]

    tableFrame = tk.Frame(window)
    
    for col, header in enumerate(headers):
        label = tk.Label(tableFrame, text=header, borderwidth=1, width=width[col], relief="solid", font=('Arial bold', 10))
        label.grid(row=0, column=col)
    
    for i in range(rows):
        for j in range(cols):
            entry = tk.Label(tableFrame, text=test_data[i][j], borderwidth=1, width=width[j], relief="solid", font=('Arial', 10))
            entry.grid(row=i + 1, column=j, sticky="nsew")
    
    tableFrame.pack(fill='x', padx=10)


if __name__ == '__main__':
    # test = MainForm()
    # Jack = EmployeeData("BDI-001", "Ethan Thompson", date(2006, 10, 23))
    # test.display()
    test_data = [(1,'Raj','Mumbai',19, 30),
       (2,'Aaryan','Pune',18, 30),
       (3,'Vaishnavi','Mumbai',20, 30),
       (4,'Rachna','Mumbai',21, 30),
       (5,'Shubham','Delhi',21, 30)]


    window = tk.Tk()
    win_initialize(window)
    initialize_ui(window)
    window.mainloop()
