from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class myBMIApp():
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
    def insert_data(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        contact = self.contact_entry.get()
        dob = self.birthdate_entry.get()
        occupation = self.occupation_entry.get()

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
        
        self.clear_entries()
        if(result):
            messagebox.showinfo(title='Message Alert', message=name +"'s details had been saved successfully!")
        else:
            messagebox.showerror(title='Message Alert', message="Patient details was not saved successfully!")


    def clear_entries(self):
        self.name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.birthdate_entry.delete(0, END)
        self.occupation_entry.delete(0, END)


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





    # /////////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////////////////////////////////////////////////////////////////////

    #Checking BMI Page

    # Command Function
    def view_patient_data(self):
        global patient_contact
        patient_contact = self.contact_check_entry.get()
        
        # Connect to SQLite database
        conn = sqlite3.connect("mass_hospital.db")
        cursor = conn.cursor()

        # Fetch data from the database
        cursor.execute("SELECT name FROM patients WHERE contact='"+patient_contact+"'")
        data = cursor.fetchall()

        # Clear previous entries in the treeview
        for row in self.treeview_view.get_children():
            self.treeview_view.delete(row)

        # Insert fetched data into treeview
        for record in data:
            self.treeview_view.insert("", "end", values=record)

        print(patient_contact)
        print(data)
        conn.close()
        self.contact_check_entry.delete(0, END)


    def calculate_bmi(self):
        global bmi
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get()) / 100  # convert height from cm to meters
        bmi = weight / (height * height)
        self.result_label.config(text="Patient's BMI is {:.1f}".format(bmi))
        if bmi < 18.5:
            self.status_label.config(text="Underweight", fg="blue")
        elif bmi >= 18.5 and bmi < 25:
            self.status_label.config(text="Normal weight", fg="green")
        elif bmi >= 25 and bmi < 30:
            self.status_label.config(text="Overweight", fg="orange")
        else:
            self.status_label.config(text="Obese", fg="red")

    # Save Patient BMI
    def save_bmi(self):

        # Connect to SQLite database
        conn = sqlite3.connect("mass_hospital.db")
        cursor = conn.cursor()


        # update database with bmi record into table
        
        result = cursor.execute("UPDATE patients SET BMI = ? WHERE contact = ?", (bmi, str(patient_contact)))
        
        conn.commit()
        conn.close()
        
        self.clear_bmi_entries()
        if(result):
            messagebox.showinfo(title='Message Alert', message="Patient's bmi details had been saved successfully!")
        else:
            messagebox.showerror(title='Message Alert', message="Patient's details was not saved successfully!")


    def clear_bmi_entries(self):
        self.weight_entry.delete(0, END)
        self.height_entry.delete(0, END)
        self.status_label.config(text="")


    # Title
    title = Label(master=checkingBMITab, text='Mass Hospital BMI Checking', font=(20)) #
    title.grid(row=0, column=0, padx=50, pady=20, sticky=W+E)

    # Create a label frame
    labelViewPatientDetails =LabelFrame(master=checkingBMITab)
    labelViewPatientDetails.grid(row=1, column=0, padx=50, pady=5,)




    # Create labels and entry widgets
    contact_label = Label(labelViewPatientDetails, text="Contact")
    contact_label.grid(row=0, column=0, padx=0, pady=5)

    contact_check_entry = Entry(labelViewPatientDetails, width=40)
    contact_check_entry.grid(row=0, column=1, padx=0, pady=5,)

    search_detail_btn = Button(labelViewPatientDetails, width=10, text="Serach", command=view_patient_data)
    search_detail_btn.grid(row=0, column=2, padx=0, pady=5,)


    # Create Treeview widget with scrollbar
    treeview_frame = LabelFrame(labelViewPatientDetails)
    treeview_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


    treeview_view = ttk.Treeview(treeview_frame, columns=("Name"))
    treeview_view.grid(row=2, column=0, columnspan=2,)


    # Set column headings
    treeview_view.heading("#0", text="")
    treeview_view.heading("#1", text="Name")




    # Create a label frame
    labelframeBMI =LabelFrame(master=checkingBMITab)
    labelframeBMI.grid(row=2, column=0, padx=50, pady=5,)

    # Create labels and entry widgets
    weight_label = Label(labelframeBMI, text="Weight (kg):")
    weight_label.grid(row=0, column=0, padx=10, pady=5)
    weight_entry = Entry(labelframeBMI, width=40)
    weight_entry.grid(row=0, column=1, padx=10, pady=5,)

    height_label = Label(labelframeBMI, text="Height (cm):")
    height_label.grid(row=1, column=0, padx=10, pady=5)
    height_entry = Entry(labelframeBMI, width=40)
    height_entry.grid(row=1, column=1, padx=10, pady=5)

    result_label = Label(labelframeBMI, text="")
    result_label.grid(row=2, columnspan=2, padx=10, pady=5)

    status_label = Label(labelframeBMI, text="")
    status_label.grid(row=3, columnspan=2, padx=10, pady=5)

    calculate_button = Button(labelframeBMI, text="Calculate BMI", width=35, bg='green', fg='white', command=calculate_bmi)
    calculate_button.grid(row=4, columnspan=2, padx=10, pady=(5, 20))

    save_record_button = Button(labelframeBMI, text="Save BMI", width=35, bg='blue', fg='white', command=save_bmi)
    save_record_button.grid(row=5, columnspan=2, padx=10, pady=(5, 20))



    # /////////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////////////////////////////////////////////////////////////////////
    # /////////////////////////////////////////////////////////////////////////////////////////

    #View Patient Records Page

    def fetch_data(self):
        # Connect to SQLite database
        conn = sqlite3.connect("mass_hospital.db")
        cursor = conn.cursor()

        

        # Fetch data from the database
        cursor.execute("SELECT name, email, contact, dob, occupation, BMI  FROM patients WHERE contact='"+self.search_entry.get()+"'")
        data = cursor.fetchall()

        # Clear previous entries in the treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Insert fetched data into treeview
        for record in data:
            self.treeview.insert("", "end", values=record)

        conn.close()
        self.search_entry.delete(0, END)

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