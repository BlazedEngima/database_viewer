import tkinter as tk
from datetime import date
from dateutil import relativedelta


class MainForm:
    def __init__(self, window=None, tableFrame=None, buttonFrame=None, employeeList=[], start_p=0):
        self.dtmToday = date.today()
        self.employeeList = employeeList
        self.start_p = start_p
        self.window = window
        self.tableFrame = tableFrame
        self.buttonFrame = buttonFrame

        self.headers = ['NO', 'ID', 'NAME', 'BIRTHDAY', 'AGE']
        self.width = [5, 15, 25, 20, 30]
        self.button_icon = ['|<', '<<', '<', '>', '>>', '>|']
        self.button_dict = {}
        self.label_dict = {}

        self.data_alignment = ['e', 'w', 'w', 'center', 'center']
        self.rows, self.cols = 5, 5

    def _init_buttonFrame(self):
        jump_distance = [-len(self.employeeList), -5, -1, 1, 5, len(self.employeeList)]

        for i in range(6):
            name = self.button_icon[i]
            distance = jump_distance[i]

            def action(x = distance):
                return self._button_function(x)

            self.button_dict[name] = tk.Button(self.buttonFrame, text=self.button_icon[i], width=5, font=('Arial bold', 10), command=action)
            self.button_dict[name].grid(row=0, column=i)
        
        self.buttonFrame.pack(fill='x', padx=10, pady=20)

    def _init_tableFrame(self):
        for col, header in enumerate(self.headers):
            label = tk.Label(self.tableFrame, text=header, borderwidth=1, width=self.width[col], relief="solid", font=('Arial bold', 10), padx=5)
            label.grid(row=0, column=col)
        
        for i in range(self.rows):
            for j in range(self.cols):
                text_val = self._get_column_data(i, j)
                self.label_dict[(i, j)] = tk.Label(self.tableFrame, text=text_val, borderwidth=1, width=self.width[j], relief="solid", font=('Arial', 10), anchor=self.data_alignment[j], padx=5)
                self.label_dict[(i, j)].grid(row=i + 1, column=j, sticky='nsew')

        self.tableFrame.pack(fill='x', padx=10)

    def _update(self):
        
        for i in range(self.rows):
            for j in range(self.cols):
                text_val = self._get_column_data(i, j)
                self.label_dict[(i, j)]['text'] = text_val
                
    def _get_column_data(self, i, j):
        if j == 0:
            return str(self.start_p + i + 1)

        elif j == 4:
            birth_date = self.employeeList[self.start_p + i][3]
            delta = relativedelta.relativedelta(self.dtmToday, birth_date)

            return f'{delta.years} Year {delta.months} Month {delta.days} Day' 

        return self.employeeList[self.start_p + i][j]

    def _move_pointer(self, value):
        if self.start_p + value <= 0:
            self.start_p = 0

        elif self.start_p + value + 5 >= len(self.employeeList):
            self.start_p = len(self.employeeList) - 5
        
        else:
            self.start_p += value

    def _button_function(self, value):
        self._move_pointer(value=value)
        self._update()

    def add(self, employeeData):
        self.employeeList.append(employeeData)

    def win_initialize(self):
        self.window.geometry("840x240")
        self.window.title("Main")

        curr_date = tk.Label(self.window, text=date.today(), font=('Arial Bold', 10))
        curr_date.pack(padx=10, pady=10, anchor='w')
        
    def initialize_ui(self):
        self._init_tableFrame()
        self._init_buttonFrame()

    def button_commands(self, value):
        self._move_pointer(value)
        self._update()

    def initialize_data(self):
        self.add(EmployeeData("BDI-001", "Ethan Thompson", date(2006, 10, 23)));
        self.add(EmployeeData("BDI-002", "Ava Williams", date(2010, 11, 26)));
        self.add(EmployeeData("BDI-003", "Benjamin Davis", date(2007, 10, 24)));
        self.add(EmployeeData("BDI-004", "Olivia Martinez", date(2002, 8, 19)));
        self.add(EmployeeData("BDI-005", "Liam Garcia", date(1998, 7, 16)));
        self.add(EmployeeData("BDI-006", "Mia Smith", date(1996, 6, 14)));
        self.add(EmployeeData("BDI-007", "Samuel Johnson", date(2010, 11, 26)));
        self.add(EmployeeData("BDI-008", "Sophia Harris", date(2004, 9, 21)));
        self.add(EmployeeData("BDI-009", "Daniel Lee", date(1982, 1, 2)));
        self.add(EmployeeData("BDI-010", "Charlotte Turner", date(2003, 9, 20)));
        self.add(EmployeeData("BDI-011", "Henry Martin", date(1994, 5, 13)));
        self.add(EmployeeData("BDI-012", "Amelia Lewis", date(1985, 2, 5)));
        self.add(EmployeeData("BDI-013", "Jackson Robinson", date(1981, 1, 2)));
        self.add(EmployeeData("BDI-014", "Harper Clark", date(1996, 6, 15)));
        self.add(EmployeeData("BDI-015", "Lucas King", date(1984, 2, 5)));
        self.add(EmployeeData("BDI-016", "Evelyn Hall", date(2004, 9, 21)));
        self.add(EmployeeData("BDI-017", "Alexander Young", date(1986, 3, 6)));
        self.add(EmployeeData("BDI-018", "Grace Turner", date(1980, 1, 1)));
        self.add(EmployeeData("BDI-019", "William Adams", date(2004, 9, 21)));
        self.add(EmployeeData("BDI-020", "Victoria Baker", date(2006, 10, 23)));
        self.add(EmployeeData("BDI-021", "James Hall", date(1996, 6, 15)));
        self.add(EmployeeData("BDI-022", "Zoe Lewis", date(2010, 11, 27)));
        self.add(EmployeeData("BDI-023", "Benjamin Reed", date(1990, 4, 10)));
        self.add(EmployeeData("BDI-024", "Mia Collins", date(1997, 7, 16)));
        self.add(EmployeeData("BDI-025", "Samuel White", date(1990, 4, 9)));
        self.add(EmployeeData("BDI-026", "Ava Phillips", date(1980, 1, 1)));
        self.add(EmployeeData("BDI-027", "David Rodriguez", date(1986, 3, 6)));
        self.add(EmployeeData("BDI-028", "Lily Green", date(1980, 1, 1)));
        self.add(EmployeeData("BDI-029", "Henry Turner", date(2010, 11, 26)));
        self.add(EmployeeData("BDI-030", "Chloe Smith", date(2000, 8, 18)));
        self.add(EmployeeData("BDI-031", "Michael Campbell", date(2004, 9, 21)));
        self.add(EmployeeData("BDI-032", "Emily Anderson", date(2011, 11, 27)));
        self.add(EmployeeData("BDI-033", "John Hernandez", date(2006, 10, 23)));
        self.add(EmployeeData("BDI-034", "Abigail Scott", date(2008, 10, 25)));
        self.add(EmployeeData("BDI-035", "Daniel Perez", date(1998, 7, 16)));
        self.add(EmployeeData("BDI-036", "Ella Collins", date(1990, 4, 9)));
        self.add(EmployeeData("BDI-037", "Matthew Sanchez", date(1981, 1, 2)));
        self.add(EmployeeData("BDI-038", "Scarlett Taylor", date(1995, 6, 13)));
        self.add(EmployeeData("BDI-039", "Samuel Mitchell", date(1996, 6, 14)));
        self.add(EmployeeData("BDI-040", "Sophia Nelson", date(2008, 10, 25)));
        self.add(EmployeeData("BDI-041", "David Brown", date(2005, 9, 22)));
        self.add(EmployeeData("BDI-042", "Harper Johnson", date(2004, 9, 21)));
        self.add(EmployeeData("BDI-043", "Christopher Ross", date(2006, 9, 22)));
        self.add(EmployeeData("BDI-044", "Amelia Moore", date(1993, 5, 12)));
        self.add(EmployeeData("BDI-045", "Logan Mitchell", date(1991, 5, 10)));
        self.add(EmployeeData("BDI-046", "Elizabeth Cooper", date(1983, 2, 3)));
        self.add(EmployeeData("BDI-047", "Andrew Foster", date(1994, 6, 13)));
        self.add(EmployeeData("BDI-048", "Madison Turner", date(1996, 6, 14)));
        self.add(EmployeeData("BDI-049", "Benjamin Flores", date(1997, 7, 15)));
        self.add(EmployeeData("BDI-050", "Penelope Butler", date(2005, 9, 22)));
        self.add(EmployeeData("BDI-051", "Samuel Scott", date(1997, 7, 16)));
        self.add(EmployeeData("BDI-052", "Emily Nelson", date(1999, 7, 17)));
        self.add(EmployeeData("BDI-053", "Joseph Rivera", date(1993, 5, 12)));
        self.add(EmployeeData("BDI-054", "Avery Turner", date(1985, 2, 5)));
        self.add(EmployeeData("BDI-055", "William Cox", date(1996, 6, 15)));
        self.add(EmployeeData("BDI-056", "Sofia Garcia", date(2007, 10, 24)));
        self.add(EmployeeData("BDI-057", "Ethan Baker", date(1999, 7, 17)));
        self.add(EmployeeData("BDI-058", "Grace Adams", date(1989, 4, 8)));
        self.add(EmployeeData("BDI-059", "Daniel Coleman", date(1991, 5, 10)));
        self.add(EmployeeData("BDI-060", "Harper Jenkins", date(1997, 7, 16)));
        self.add(EmployeeData("BDI-061", "Aiden Phillips", date(1989, 4, 9)));
        self.add(EmployeeData("BDI-062", "Mia Turner", date(2009, 11, 26)));
        self.add(EmployeeData("BDI-063", "Benjamin Lewis", date(2005, 9, 22)));
        self.add(EmployeeData("BDI-064", "Chloe Martinez", date(1993, 5, 12)));
        self.add(EmployeeData("BDI-065", "Samuel Adams", date(2011, 11, 27)));
        self.add(EmployeeData("BDI-066", "Lily Turner", date(1994, 6, 13)));
        self.add(EmployeeData("BDI-067", "Alexander Peterson", date(1990, 4, 10)));
        self.add(EmployeeData("BDI-068", "Amelia Reed", date(1984, 2, 5)));
        self.add(EmployeeData("BDI-069", "Michael White", date(2010, 11, 26)));
        self.add(EmployeeData("BDI-070", "Olivia Turner", date(2006, 10, 23)));
        self.add(EmployeeData("BDI-071", "James Hernandez", date(2002, 8, 19)));
        self.add(EmployeeData("BDI-072", "Zoe Anderson", date(2003, 9, 20)));
        self.add(EmployeeData("BDI-073", "William Collins", date(1996, 6, 14)));
        self.add(EmployeeData("BDI-074", "Emily Roberts", date(2007, 10, 24)));
        self.add(EmployeeData("BDI-075", "Jackson Lewis", date(1980, 1, 1)));
        self.add(EmployeeData("BDI-076", "Grace Carter", date(2004, 9, 21)));
        self.add(EmployeeData("BDI-077", "David Martinez", date(1984, 2, 5)));
        self.add(EmployeeData("BDI-078", "Ava Reed", date(2008, 10, 25)));
        self.add(EmployeeData("BDI-079", "Henry Thompson", date(1986, 3, 6)));
        self.add(EmployeeData("BDI-080", "Sophia Turner", date(1987, 3, 7)));
        self.add(EmployeeData("BDI-081", "Christopher Lee", date(1997, 7, 16)));
        self.add(EmployeeData("BDI-082", "Charlotte King", date(2002, 8, 19)));
        self.add(EmployeeData("BDI-083", "Samuel Campbell", date(1995, 6, 13)));
        self.add(EmployeeData("BDI-084", "Harper Turner", date(1984, 2, 5)));
        self.add(EmployeeData("BDI-085", "Benjamin Wright", date(1983, 2, 3)));
        self.add(EmployeeData("BDI-086", "Mia Davis", date(1985, 2, 5)));
        self.add(EmployeeData("BDI-087", "Michael Turner", date(1998, 7, 16)));
        self.add(EmployeeData("BDI-088", "Elizabeth Hall", date(2001, 8, 18)));
        self.add(EmployeeData("BDI-089", "Ethan Green", date(1992, 5, 11)));
        self.add(EmployeeData("BDI-090", "Lily Martinez", date(2002, 8, 19)));
        self.add(EmployeeData("BDI-091", "Alexander Scott", date(2002, 8, 20)));
        self.add(EmployeeData("BDI-092", "Abigail Turner", date(2004, 9, 21)));
        self.add(EmployeeData("BDI-093", "Daniel Adams", date(1983, 2, 4)));
        self.add(EmployeeData("BDI-094", "Grace Johnson", date(2010, 11, 26)));
        self.add(EmployeeData("BDI-095", "William Turner", date(1998, 7, 16)));
        self.add(EmployeeData("BDI-096", "Mia Moore", date(2007, 10, 24)));
        self.add(EmployeeData("BDI-097", "James Johnson", date(2010, 11, 26)));
        self.add(EmployeeData("BDI-098", "Zoe White", date(1992, 5, 11)));
        self.add(EmployeeData("BDI-099", "Samuel Smith", date(1994, 6, 13)));
        self.add(EmployeeData("BDI-100", "Emily Turner", date(2008, 10, 25)));
        self.add(EmployeeData("BDI-101", "Benjamin Mitchell", date(2004, 9, 21)));
        self.add(EmployeeData("BDI-102", "Ava Turner", date(1989, 4, 9)));
        self.add(EmployeeData("BDI-103", "Christopher Turner", date(1997, 7, 16)));
        self.add(EmployeeData("BDI-104", "Sophia Davis", date(2003, 8, 20)));
        self.add(EmployeeData("BDI-105", "David Scott", date(1983, 2, 3)));
        self.add(EmployeeData("BDI-106", "Harper Martinez", date(2006, 10, 23)));
        self.add(EmployeeData("BDI-107", "Henry Turner", date(1982, 2, 3)));
        self.add(EmployeeData("BDI-108", "Olivia Adams", date(1997, 7, 16)));
        self.add(EmployeeData("BDI-109", "Alexander Reed", date(1984, 2, 4)));
        self.add(EmployeeData("BDI-110", "Amelia Turner", date(2004, 9, 21)));
        self.add(EmployeeData("BDI-111", "Samuel Turner", date(2002, 8, 20)));
        self.add(EmployeeData("BDI-112", "Grace Hernandez", date(2003, 8, 20)));
        self.add(EmployeeData("BDI-113", "Michael Collins", date(1983, 2, 3)));
        self.add(EmployeeData("BDI-114", "Mia Turner", date(1984, 2, 4)));
        self.add(EmployeeData("BDI-115", "Benjamin Turner", date(1980, 1, 1)));
        self.add(EmployeeData("BDI-116", "Emily Martin", date(1999, 7, 17)));
        self.add(EmployeeData("BDI-117", "William Nelson", date(1994, 6, 13)));
        self.add(EmployeeData("BDI-118", "Ava Anderson", date(2000, 8, 18)));
        self.add(EmployeeData("BDI-119", "James Turner", date(1990, 4, 9)));
        self.add(EmployeeData("BDI-120", "Charlotte Lewis", date(2005, 9, 22)));
        self.add(EmployeeData("BDI-121", "Samuel Garcia", date(2008, 10, 25)));
        self.add(EmployeeData("BDI-122", "Olivia Carter", date(2001, 8, 19)));
        self.add(EmployeeData("BDI-123", "Alexander Turner", date(2004, 9, 21)));

    #Test function
    def display(self):
        print(self.employeeList[0][3])

class EmployeeData:
    def __init__(self, szId = '', szName = '', dtmBirthday = date.min):
        self.szId = szId
        self.szName = szName
        self.dtmBirthday = dtmBirthday

    def __getitem__(self, index):
        if index == 1:
            return self.szId
        if index == 2:
            return self.szName
        if index == 3:
            return self.dtmBirthday
        
        return IndexError
            
if __name__ == '__main__':
    test_data = [(1,'Raj','Mumbai',19, 30),
       (2,'Aaryan','Pune',18, 30),
       (3,'Vaishnavi','Mumbai',20, 30),
       (4,'Rachna','Mumbai',21, 30),
       (5,'Shubham','Delhi',21, 30)]


    root = tk.Tk()

    tableFrame, buttonFrame = tk.Frame(root), tk.Frame(root)
    window = MainForm(window=root, tableFrame=tableFrame, buttonFrame=buttonFrame)

    window.win_initialize()
    window.initialize_data()
    window.initialize_ui()

    root.mainloop()
