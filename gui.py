from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkcalendar import DateEntry
import datetime

today = datetime.date.today()

#btn commands
def Update_Cash_Flow():
    exp = Expense_Total.get()
    inc = Income_Total.get()

    cash_flow = inc - exp

    Cash_Flow.set(cash_flow)

def AddExpense():
    a = EDate.get()
    b = Title.get()
    c = float(Expense.get())

    TVExpense.insert('', 'end',values=[a,b,c])
    
    tempExp = Expense_Total.get()
    tempExp += c
    Expense_Total.set(tempExp)

    Update_Cash_Flow()

    Title.set('')
    Expense.set(0)
    EDate.set_date(today)

def DeleteExpense():
    selected_row = TVExpense.selection()[0]
    selected_values = TVExpense.item(selected_row)

    TVExpense.delete(selected_row)

    delta = float(selected_values['values'][2])
    tempExp = Expense_Total.get()
    tempExp -= delta
    Expense_Total.set(tempExp)

    Update_Cash_Flow()

def ClearExpenses():
    TVExpense.delete(*TVExpense.get_children())
    Expense_Total.set(0)

    Update_Cash_Flow()

def AddIncome():
    a = NDate.get()
    b = Right_Title.get()
    c = float(Income.get())

    TVIncome.insert('', 'end', values=[a,b,c])
    tempInc = Income_Total.get()
    tempInc += c
    Income_Total.set(tempInc)

    Update_Cash_Flow()
    
    Income.set(0)
    Right_Title.set('')
    NDate.set_date(today)

def DeleteIncome():
    selected_row = TVIncome.selection()[0]
    selected_values = TVIncome.item(selected_row)

    TVIncome.delete(selected_row)

    delta = float(selected_values['values'][2])
    tempInc = Income_Total.get()
    tempInc -= delta
    Income_Total.set(tempInc)

    Update_Cash_Flow()
    

def ClearIncome():
    TVIncome.delete(*TVIncome.get_children())
    Income_Total.set(0)

    Update_Cash_Flow()

GUI = Tk()
GUI.title('Expense and Income Recorder')
GUI.geometry('700x500')
#Maximize window
# GUI.state('zoomed')

Tab = Notebook(GUI)

F1 = Frame(Tab, width=500,height=500)
F2 = Frame(Tab, width=500,height=500)
F3 = Frame(Tab, width=500,height=500)

Tab.add(F1, text='Expense')
Tab.add(F2, text='Income')
Tab.add(F3, text='Summary')

Tab.pack(fill=BOTH, expand=1)

# Tab 1 (Expense)
# ----------Row 0--------------
LDate = ttk.Label(F1, text='Date', font=(None,18))
LDate.grid(row=0, column=0, padx=5, pady=5, sticky='w')

#use date picker
#pip install tkcalendar
EDate = DateEntry(F1, width=19, background='blue', foreground='white', font=(None,18))
EDate.grid(row=0, column=1, padx=5, pady=5, sticky='w', columnspan=2)

# ----------Row 1--------------
LTitle = ttk.Label(F1, text='Title', font=(None,18))
LTitle.grid(row=1, column=0, padx=5, pady=5, sticky='w')

Title = StringVar()

ETitle = ttk.Entry(F1, textvariable=Title,font=(None,18))
ETitle.grid(row=1, column=1, padx=5, pady=5, sticky='w', columnspan=2)

# ----------Row 2--------------
LExpense = ttk.Label(F1, text='Expense', font=(None,18))
LExpense.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Expense = StringVar()

EExpense = ttk.Entry(F1, textvariable=Expense,font=(None,18))
EExpense.grid(row=2, column=1, padx=5, pady=5, sticky='w', columnspan=2)

# ----------Row 3--------------
BF1Add = ttk.Button(F1, text='Add',command=AddExpense)
BF1Add.grid(row=3,column=1,padx=2,pady=5,sticky='w',ipadx=10,ipady=10)

BF1Delete = ttk.Button(F1, text="Delete", command=DeleteExpense)
BF1Delete.grid(row=3,column=2, padx=2, pady=5, sticky='w', ipadx=10, ipady=10)

BF1Clear = ttk.Button(F1, text="Clear",command=ClearExpenses)
BF1Clear.grid(row=3,column=3,padx=2,pady=5,sticky='w',ipadx=10,ipady=10)

# ----------Tree View----------
TVList = ['Date', 'Title', 'Expense']
TVExpense = ttk.Treeview(F1, column=TVList, show='headings', height=5)
for i in TVList:
    TVExpense.heading(i, text=i.title())
TVExpense.grid(row=4,column=0,padx=5,pady=5,sticky='w',columnspan=3)

# End Tab 1 (Expense)
##############################################################
#Tab 2 (Income)
# ----------Row 0--------------
RDate = ttk.Label(F2, text='Date', font=(None,18))
RDate.grid(row=0, column=0, padx=5, pady=5, sticky='w')

#use date picker
#pip install tkcalendar
NDate = DateEntry(F2, width=19, background='blue', foreground='white', font=(None,18))
NDate.grid(row=0, column=1, padx=5, pady=5, sticky='w', columnspan=2)

# ----------Row 1--------------
RTitle = ttk.Label(F2, text='Title', font=(None,18))
RTitle.grid(row=1, column=0, padx=5, pady=5, sticky='w')

Right_Title = StringVar()

NTitle = ttk.Entry(F2, textvariable=Right_Title,font=(None,18))
NTitle.grid(row=1, column=1, padx=5, pady=5, sticky='w', columnspan=2)

# ----------Row 2--------------
RIncome = ttk.Label(F2, text='Income', font=(None,18))
RIncome.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Income = StringVar()

NIncome = ttk.Entry(F2, textvariable=Income,font=(None,18))
NIncome.grid(row=2, column=1, padx=5, pady=5, sticky='w', columnspan=2)

# ----------Row 3--------------
BF2Add = ttk.Button(F2, text='Add',command=AddIncome)
BF2Add.grid(row=3,column=1,padx=2,pady=5,sticky='w',ipadx=10,ipady=10)

BF1Delete = ttk.Button(F2, text="Delete", command=DeleteIncome)
BF1Delete.grid(row=3,column=2, padx=2, pady=5, sticky='w', ipadx=10, ipady=10)

BF2Delete = ttk.Button(F2, text="Clear",command=ClearIncome)
BF2Delete.grid(row=3,column=3,padx=2,pady=5,sticky='w',ipadx=10,ipady=10)

# ----------Tree View----------
TVList_Income = ['Date', 'Title', 'Income']
TVIncome = ttk.Treeview(F2, column=TVList_Income, show='headings', height=5)
for i in TVList_Income:
    TVIncome.heading(i, text=i.title())
TVIncome.grid(row=4,column=0,padx=5,pady=5,sticky='w',columnspan=3)
#End Tab 2 (Income)
########################################################
#Tab 3 (Summary)
#----------Row 1-----------------
Income_Total_Label = ttk.Label(F3, text='Total Income', font=(None,18))
Income_Total_Label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

Income_Total = DoubleVar()

Income_Total_Entry = ttk.Entry(F3, textvariable=Income_Total,font=(None,18),state='disabled')
Income_Total_Entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

#---------Row 2------------------
Expense_Total_Label = ttk.Label(F3, text='Total Expense', font=(None,18))
Expense_Total_Label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

Expense_Total = DoubleVar()

Expense_Total_Entry = ttk.Entry(F3, textvariable=Expense_Total,font=(None,18),state='disabled')
Expense_Total_Entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

#---------Row 3------------------
Cash_Flow_Label = ttk.Label(F3, text='Cash Flow', font=(None,18))
Cash_Flow_Label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Cash_Flow = DoubleVar()

Cash_Flow_Entry = ttk.Entry(F3, textvariable=Cash_Flow,font=(None,18),state='disabled')
Cash_Flow_Entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')


#End Tab 3 (Summary)







#end GUI
GUI.mainloop()