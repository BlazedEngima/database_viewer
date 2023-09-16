import tkinter as tk
from datetime import date

class MainForm:
    def __init__(self, window, employeeList = [], uiList = [None] * 5):
        self.dtmToday = date.today()
        self.employeeList = employeeList
        self.uiList = uiList
        self.window = window
        self.headers = ['NO', 'ID', 'NAME', 'BIRTHDAY', 'AGE']
        self.width = [10, 15, 25, 20, 30]
        self.button_icon = ['|<', '<<', '<', '>', '>>', '>|']
    
    def add_employee(self, employeeData):
        self.employeeList.append(employeeData)

    def add_ui(self, uiElement):
        self.uiList.append(uiElement)

    def remove_ui(self, index):
        self.uiList[index] = None

    def win_initialize(self):
        self.window.geometry("840x240")
        self.window.title("Main")

        curr_date = tk.Label(self.window, text=date.today(), font=('Arial Bold', 10))
        curr_date.pack(padx=10, pady=10, anchor='w')
        
    def initialize_ui(self):
        self.__init_tableFrame__()
        self.__init_buttonFrame__()

    def __init_buttonFrame__(self):
        buttonFrame = tk.Frame(self.window)

        for i in range(6):
            button = tk.Button(buttonFrame, text=self.button_icon[i], width=5, font=('Arial bold', 10))
            button.grid(row=0, column=i)
        
        buttonFrame.pack(fill='x', padx=10, pady=20)

    def __init_tableFrame__(self):
        rows, cols = 5, 5
        tableFrame = tk.Frame(self.window)
        
        for col, header in enumerate(self.headers):
            label = tk.Label(tableFrame, text=header, borderwidth=1, width=self.width[col], relief="solid", font=('Arial bold', 10))
            label.grid(row=0, column=col)
        
        for i in range(rows):
            for j in range(cols):
                entry = tk.Label(tableFrame, text=test_data[i][j], borderwidth=1, width=self.width[j], relief="solid", font=('Arial', 10))
                entry.grid(row=i + 1, column=j, sticky="nsew")
        
        tableFrame.pack(fill='x', padx=10)

    #Test function
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


if __name__ == '__main__':
    # test = MainForm()
    # Jack = EmployeeData("BDI-001", "Ethan Thompson", date(2006, 10, 23))
    # test.display()
    test_data = [(1,'Raj','Mumbai',19, 30),
       (2,'Aaryan','Pune',18, 30),
       (3,'Vaishnavi','Mumbai',20, 30),
       (4,'Rachna','Mumbai',21, 30),
       (5,'Shubham','Delhi',21, 30)]


    root = tk.Tk()

    window = MainForm(root)
    window.win_initialize()
    window.initialize_ui()

    root.mainloop()
