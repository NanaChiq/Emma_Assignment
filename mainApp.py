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

#Registration Page

# Command Function
def insert_data():
    name = name_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    dob = birthdate_entry.get()
    occupation = occupation_entry.get()

    # Connect to SQLite database
    conn = sqlite3.connect("mass_hospital.db")
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        email TEXT,
                        contact TEXT,
                        dob TEXT,
                        occupation TEXT,
                        BMI TEXT NULL
                    )''')

    # Insert data into table
    result = cursor.execute('''INSERT INTO patients (name, email, contact, dob, occupation, BMI)
                      VALUES (?, ?, ?, ?, ?, ?)''', 
                      (name, email, contact, dob, occupation, "")
                    )
    
    conn.commit()
    conn.close()
    
    clear_entries()
    if(result):
        messagebox.showinfo(title='Message Alert', message=name +"'s details had been saved successfully!")
    else:
        messagebox.showerror(title='Message Alert', message="Patient details was not saved successfully!")


def clear_entries():
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    contact_entry.delete(0, END)
    birthdate_entry.delete(0, END)
    occupation_entry.delete(0, END)


# Title
title = Label(master=registerTab, text='Mass Hospital', font=(20)) #
title.grid(row=0, column=0, padx=50, pady=5, sticky=W+E)

labelframe =LabelFrame(master=registerTab)
labelframe.grid(row=1, column=0, padx=50, pady=5,)

# Patient Name
name_lbl = Label(master=labelframe, text='Patient Name') #
name_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)

name_entry = Entry(master=labelframe, width=50) 
name_entry.grid(row=3, column=0, padx=10, pady=[0, 10], columnspan=2)

# Patient Email
email_lbl = Label(master=labelframe, text='Patient Email') #
email_lbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)

email_entry = Entry(master=labelframe, width=50) 
email_entry.grid(row=5, column=0, padx=10, pady=[0, 10], columnspan=2)

# Patient Contact
contact_lbl = Label(master=labelframe, text='Patient Contact') #
contact_lbl.grid(row=6, column=0, padx=10, pady=5, sticky=W)

# Patient Birth date
birthdate_lbl = Label(master=labelframe, text='Patient Birth Date') #
birthdate_lbl.grid(row=6, column=1, padx=10, pady=5, sticky=NW)


contact_entry = Entry(master=labelframe, width=25) 
contact_entry.grid(row=7, column=0, padx=[10, 5], pady=[0, 10])


birthdate_entry = Entry(master=labelframe, width=25) 
birthdate_entry.grid(row=7, column=1, padx=[5, 10], pady=[0, 10])

# Patient Occupation
occupation_lbl = Label(master=labelframe, text='Patient Occupation') #
occupation_lbl.grid(row=8, column=0, padx=10, pady=5, sticky=W)

occupation_entry = Entry(master=labelframe, width=50) 
occupation_entry.grid(row=9, column=0, padx=10, pady=[0, 10], columnspan=2)

# Control Buttons
clear_btn = Button(master=labelframe, text='Clear', bg='red', fg='white', width=20, command=clear_entries) 
clear_btn.grid(row=10, column=0, padx=[10, 5], pady=[20, 20])


submit_btn = Button(master=labelframe, text="Submit", bg='green', fg='white',  width=20, command=insert_data) 
submit_btn.grid(row=10, column=1, padx=[5, 10], pady=[20, 20])




root.mainloop()