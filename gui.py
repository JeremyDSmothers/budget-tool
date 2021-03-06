from sqlite3.dbapi2 import Connection
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkcalendar import DateEntry
import datetime
import sqlite3
import sys

today = datetime.date.today()

#btn commands
def Update_Cash_Flow():
    exp = Expense_Total.get()
    inc = Income_Total.get()

    cash_flow = inc - exp

    Cash_Flow.set(cash_flow)

def AddExpense():
    #get data from entry fields
    a = Expense_Date_Entry.get()
    b = Category_List[Expense_Category_Entry.current()]
    c = Expense_Title_Entry.get()
    d = float(Expense.get())

    #insert new row into tree view
    Expense_Tree_View.insert('', 'end',values=[a,b,c,d])
    
    #update cash flow tab
    tempExp = Expense_Total.get()
    tempExp += d
    Expense_Total.set(tempExp)

    Update_Cash_Flow()

    #clear entry fields
    Expense_Date_Entry.set_date(today)
    Expense_Category_Entry.current(0)
    Expense_Title.set('')
    Expense.set(0)

def DeleteExpense():
    #get currently selected row and it's values
    selected_row = Expense_Tree_View.selection()[0]
    selected_values = Expense_Tree_View.item(selected_row)

    #delete currently selected row
    Expense_Tree_View.delete(selected_row)

    #update cash flow tab based on values from deleted row
    delta = float(selected_values['values'][3])
    tempExp = Expense_Total.get()
    tempExp -= delta
    Expense_Total.set(tempExp)

    Update_Cash_Flow()

def ClearExpenses():
    Expense_Tree_View.delete(*Expense_Tree_View.get_children())
    Expense_Total.set(0)

    Update_Cash_Flow()

def AddIncome():
    #get data from entry fields
    a = Income_Date_Entry.get()
    b = Category_List[Income_Category_Entry.current()]
    c = Income_Title.get()
    d = float(Income.get())

    #insert new row into tree view
    Income_Tree_View.insert('', 'end', values=[a,b,c,d])

    #update cash flow tab
    tempInc = Income_Total.get()
    tempInc += d
    Income_Total.set(tempInc)

    Update_Cash_Flow()
    
    #clear entry fields
    Income_Date_Entry.set_date(today)
    Income_Category_Entry.current(0)
    Income_Title.set('')
    Income.set(0)

def DeleteIncome():
    #get currently selected row and it's values
    selected_row = Income_Tree_View.selection()[0]
    selected_values = Income_Tree_View.item(selected_row)

    #delete currently selected row
    Income_Tree_View.delete(selected_row)

    #update cash flow tab based on values from deleted row
    delta = float(selected_values['values'][3])
    tempInc = Income_Total.get()
    tempInc -= delta
    Income_Total.set(tempInc)

    Update_Cash_Flow()

def ClearIncome():
    Income_Tree_View.delete(*Income_Tree_View.get_children())
    Income_Total.set(0)

    Update_Cash_Flow()

def AddCategory():
    a = Category_Entry.get()

    Category_Tree_View.insert('', 'end', values=[a])

    #update other tabs' dropdowns
    UpdateComboBoxes()

    #clear entry fields
    Category.set('')

def DeleteCategory():
    #get currently selected row it's values
    selected_row = Category_Tree_View.selection()[0]
    selected_values = Category_Tree_View.item(selected_row)

    #delete row
    Category_Tree_View.delete(selected_row)

    #update other tabs' dropdowns
    UpdateComboBoxes()

def ClearCategories():
    Category_Tree_View.delete(*Category_Tree_View.get_children())
    
    #empty other tabs' dropdowns
    UpdateComboBoxes()

def UpdateComboBoxes():
    tempList = []

    for i in Category_Tree_View.get_children():
        print(Category_Tree_View.item(i)['values'])
        tempList.append(Category_Tree_View.item(i)['values'])

    Expense_Category_Entry['values'] = tempList
    Income_Category_Entry['values'] = tempList

GUI = Tk()
GUI.title('Expense and Income Recorder')
GUI.geometry('700x500')
#Maximize window
# GUI.state('zoomed')

Tab = Notebook(GUI)

F1 = Frame(Tab, width=500,height=500)
F2 = Frame(Tab, width=500,height=500)
F3 = Frame(Tab, width=500,height=500)
F4 = Frame(Tab, width=500,height=500)

Tab.add(F1, text='Expense')
Tab.add(F2, text='Income')
Tab.add(F3, text='Summary')
Tab.add(F4, text='Setup')

Tab.pack(fill=BOTH, expand=1)

# Tab 1 (Expense)
# ----------Row 0--------------
Expense_Date_Label = ttk.Label(F1, text='Date', font=(None,18))
Expense_Date_Label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

#use date picker
#pip install tkcalendar
Expense_Date_Entry = DateEntry(F1, width=19, background='blue', foreground='white', font=(None,18))
Expense_Date_Entry.grid(row=0, column=1, padx=5, pady=5, sticky='w', columnspan=2)

#-----------Row 1--------------
Expense_Category_Label = ttk.Label(F1, text="Category", font=(None,18))
Expense_Category_Label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

Expense_Category = StringVar()

Expense_Category_Entry = ttk.Combobox(F1, width=19, state='readonly', textvariable=Expense_Category, font=(None,18))
Expense_Category_Entry.grid(row=1, column=1, padx=5, pady=5, sticky='w', columnspan=2)

# ----------Row 2--------------
Expense_Title_Label = ttk.Label(F1, text='Title', font=(None,18))
Expense_Title_Label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Expense_Title = StringVar()

Expense_Title_Entry = ttk.Entry(F1, textvariable=Expense_Title,font=(None,18))
Expense_Title_Entry.grid(row=2, column=1, padx=5, pady=5, sticky='w', columnspan=2)

# ----------Row 3--------------
Expense_Label = ttk.Label(F1, text='Expense', font=(None,18))
Expense_Label.grid(row=3, column=0, padx=5, pady=5, sticky='w')

Expense = StringVar()

Expense_Entry = ttk.Entry(F1, textvariable=Expense,font=(None,18))
Expense_Entry.grid(row=3, column=1, padx=5, pady=5, sticky='w', columnspan=2)

# ----------Row 4--------------
Btn_Add_Expense = ttk.Button(F1, text='Add',command=AddExpense)
Btn_Add_Expense.grid(row=4,column=1,padx=2,pady=5,sticky='w',ipadx=10,ipady=10)

Btn_Delete_Expense = ttk.Button(F1, text="Delete", command=DeleteExpense)
Btn_Delete_Expense.grid(row=4,column=2, padx=2, pady=5, sticky='w', ipadx=10, ipady=10)

Btn_Clear_Expenses = ttk.Button(F1, text="Clear",command=ClearExpenses)
Btn_Clear_Expenses.grid(row=4,column=3,padx=2,pady=5,sticky='w',ipadx=10,ipady=10)

# ----------Tree View----------
Expense_List = ['Date', 'Category', 'Title', 'Expense']
Expense_Tree_View = ttk.Treeview(F1, columns=Expense_List, show='headings', height=5)
Expense_Tree_View.column('Date', stretch=NO, width=55)
Expense_Tree_View.column('Category', stretch=NO, width=200)
Expense_Tree_View.column('Title', stretch=NO, width=200)
Expense_Tree_View.column('Expense', stretch=NO, width=75)
for i in Expense_List:
    Expense_Tree_View.heading(i, text=i.title())
Expense_Tree_View.grid(row=5,column=0,padx=5,pady=5,sticky='w',columnspan=3)

# End Tab 1 (Expense)
##############################################################
#Tab 2 (Income)
# ----------Row 0--------------
Income_Date_Label = ttk.Label(F2, text='Date', font=(None,18))
Income_Date_Label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

#use date picker
#pip install tkcalendar
Income_Date_Entry = DateEntry(F2, width=19, background='blue', foreground='white', font=(None,18))
Income_Date_Entry.grid(row=0, column=1, padx=5, pady=5, sticky='w', columnspan=2)

#-----------Row 1--------------
Income_Category_Label = ttk.Label(F2, text="Category", font=(None,18))
Income_Category_Label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

Income_Category = StringVar()

Income_Category_Entry = ttk.Combobox(F2, width=19, state='readonly', textvariable=Income_Category, font=(None,18))
Income_Category_Entry.grid(row=1, column=1, padx=5, pady=5, sticky='w', columnspan=2)

# ----------Row 2--------------
Income_Title_Label = ttk.Label(F2, text='Title', font=(None,18))
Income_Title_Label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Income_Title = StringVar()

Income_Title_Entry = ttk.Entry(F2, textvariable=Income_Title,font=(None,18))
Income_Title_Entry.grid(row=2, column=1, padx=5, pady=5, sticky='w', columnspan=2)

# ----------Row 3--------------
Income_Label = ttk.Label(F2, text='Income', font=(None,18))
Income_Label.grid(row=3, column=0, padx=5, pady=5, sticky='w')

Income = StringVar()

Income_Entry = ttk.Entry(F2, textvariable=Income,font=(None,18))
Income_Entry.grid(row=3, column=1, padx=5, pady=5, sticky='w', columnspan=2)

# ----------Row 4--------------
Btn_Add_Income = ttk.Button(F2, text='Add',command=AddIncome)
Btn_Add_Income.grid(row=4,column=1,ipadx=10,ipady=10,sticky='w')

Btn_Delete_Income = ttk.Button(F2, text="Delete", command=DeleteIncome)
Btn_Delete_Income.grid(row=4,column=2, ipadx=10, ipady=10,sticky='w')

Btn_Clear_Incomes = ttk.Button(F2, text="Clear",command=ClearIncome)
Btn_Clear_Incomes.grid(row=4,column=3,ipadx=10,ipady=10,sticky='w')

# ----------Tree View----------
Income_List = ['Date', 'Category', 'Title', 'Income']
Income_Tree_View = ttk.Treeview(F2, column=Income_List, show='headings', height=5)
Income_Tree_View.column('Date', stretch=NO, width=55)
Income_Tree_View.column('Category', stretch=NO, width=200)
Income_Tree_View.column('Title', stretch=NO, width=200)
Income_Tree_View.column('Income', stretch=NO, width=75)
for i in Income_List:
    Income_Tree_View.heading(i, text=i.title())
Income_Tree_View.grid(row=5,column=0,padx=5,pady=5,sticky='w',columnspan=3)
#End Tab 2 (Income)
########################################################
#Tab 3 (Summary)
#----------Row 0-----------------
Income_Total_Label = ttk.Label(F3, text='Total Income', font=(None,18))
Income_Total_Label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

Income_Total = DoubleVar()

Income_Total_Entry = ttk.Entry(F3, textvariable=Income_Total,font=(None,18),state='disabled')
Income_Total_Entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

#---------Row 1------------------
Expense_Total_Label = ttk.Label(F3, text='Total Expense', font=(None,18))
Expense_Total_Label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

Expense_Total = DoubleVar()

Expense_Total_Entry = ttk.Entry(F3, textvariable=Expense_Total,font=(None,18),state='disabled')
Expense_Total_Entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

#---------Row 2------------------
Cash_Flow_Label = ttk.Label(F3, text='Cash Flow', font=(None,18))
Cash_Flow_Label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Cash_Flow = DoubleVar()

Cash_Flow_Entry = ttk.Entry(F3, textvariable=Cash_Flow,font=(None,18),state='disabled')
Cash_Flow_Entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
#End Tab 3 (Summary)
########################################################
#Tab 4 (Setup)
#----------Row 0-----------------
Category_Label = ttk.Label(F4, text="Category", font=(None,18))
Category_Label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

Category = StringVar()

Category_Entry = ttk.Entry(F4, textvariable=Category, font=(None,18))
Category_Entry.grid(row=0, column=1, padx=5, pady=5, sticky='w', columnspan=2)

#-----------Row 1----------------
Btn_Add_Category = ttk.Button(F4, text='Add',command=AddCategory)
Btn_Add_Category.grid(row=1,column=1,padx=2,pady=5,sticky='w',ipadx=10,ipady=10)

Btn_Delete_Category = ttk.Button(F4, text="Delete", command=DeleteCategory)
Btn_Delete_Category.grid(row=1,column=2, padx=2, pady=5, sticky='w', ipadx=10, ipady=10)

Btn_Clear_Category = ttk.Button(F4, text="Clear",command=ClearCategories)
Btn_Clear_Category.grid(row=1,column=3,padx=2,pady=5,sticky='w',ipadx=10,ipady=10)

#-----------Tree View------------
Category_List = ['Category']
Category_Tree_View = ttk.Treeview(F4, columns=Category_List, show='headings', height=5)
for i in Category_List:
    Category_Tree_View.heading(i, text=i.title())
Category_Tree_View.grid(row=2, column=0, padx=5, pady=5, sticky='w', columnspan=3)
#End Tab 4 (Setup)

#end GUI
GUI.mainloop()