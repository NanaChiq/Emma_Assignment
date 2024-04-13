from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


root = Tk()
root.title('BMI App')
root.geometry("600x600")
root.maxsize=(100, 100)
root.resizable=(False, False)

#Create the notebook class for the tab widget
notebook = ttk.Notebook(master=root)

#Create the tabs
registerTab = Frame(master=notebook)
checkingBMITab = Frame(master=notebook)
viewRecordTab = Frame(master=notebook)

#Add the tabs to the notebook
notebook.add(child=registerTab, text="Registration")
notebook.add(child=checkingBMITab, text="BMT")
notebook.add(child=viewRecordTab, text="View")

#Put on the window
notebook.pack(expand=True, fill=BOTH)





root.mainloop()