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





# /////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////

#View Patient Records Page

def fetch_data():
    # Connect to SQLite database
    conn = sqlite3.connect("mass_hospital.db")
    cursor = conn.cursor()

    

    # Fetch data from the database
    cursor.execute("SELECT name, email, contact, dob, occupation, BMI  FROM patients WHERE contact='"+search_entry.get()+"'")
    data = cursor.fetchall()

    # Clear previous entries in the treeview
    for row in treeview.get_children():
        treeview.delete(row)

    # Insert fetched data into treeview
    for record in data:
        treeview.insert("", "end", values=record)

    conn.close()
    search_entry.delete(0, END)

# Create a Search Entry widget
search_label = Label(viewRecordTab, text="Patient Contact")
search_label.pack(padx=10, pady=5)
search_entry = Entry(viewRecordTab, width=40)
search_entry.pack(padx=10, pady=5)

# Create Treeview widget with scrollbar
treeview_frame = LabelFrame(viewRecordTab)
treeview_frame.pack(padx=10, pady=10)

treeview_scrollbar = Scrollbar(treeview_frame, orient='vertical')
treeview_scrollbar.pack(side=RIGHT, fill=Y)

treeview_scrollbar = Scrollbar(treeview_frame, orient='horizontal')
treeview_scrollbar.pack(side=BOTTOM, fill=X)


treeview = ttk.Treeview(treeview_frame, columns=("Name", "Email", "Contact", "Date of birth", "Occupation", "BMI"),
                        xscrollcommand=treeview_scrollbar.set,
                        yscrollcommand=treeview_scrollbar.set)
treeview.pack()

treeview_scrollbar.config(command=treeview.yview)
treeview_scrollbar.config(command=treeview.xview)

# Set column headings
#treeview.heading("#0", text="ID")
treeview.heading("#1", text="Name")
treeview.heading("#2", text="Email")
treeview.heading("#3", text="Contact")
treeview.heading("#4", text="Date of birth")
treeview.heading("#5", text="Occupation")
treeview.heading("#6", text="BMI")


# Fetch data button
fetch_button = Button(viewRecordTab, text="View records", width=40, bg='blue', fg='white', command=fetch_data)
fetch_button.pack(padx=10, pady=5)


root.mainloop()