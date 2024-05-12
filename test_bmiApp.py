import unittest
import sqlite3
from mainApp import *



#class TestDataApp(unittest.TestCase):

############################################################################
############################################################################
############################################################################
############################################################################

# Testing if inserting of patient data into database is function
def test_insertingPatientData():
    # Insert dummy data
    name = "Emma Test"
    email = "emma@test.com"
    contact = "0252525625"
    dob = "02/10/2019"
    occupation = "Techer"

    # Connect to SQLite database 
    #conn = sqlite3.connect("mass_hospital.db")
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
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
    
    if(result):
        print("Inserting of patient into database is Okay")
    else:
        print("Inserting of patient into database failed")


############################################################################
############################################################################
############################################################################
############################################################################

# Testing if retrival of patient's data is function
def test_retrivalOfPatientData():
    global patient_contact
    patient_contact = "023333333"
    
    # Connect to SQLite database
    conn = sqlite3.connect("mass_hospital.db")
    cursor = conn.cursor()

    # Fetch data from the database
    cursor.execute("SELECT name FROM patients WHERE contact='"+patient_contact+"'")
    data = cursor.fetchall()

    # Check assert of the result
    assert len(data) == 1

    if(len(data) == 1):
        print("Retrival of patient data is okay")
    else:
        print("Retrival of patient data failed")

    conn.close()

############################################################################
############################################################################
############################################################################
############################################################################

# Checking if Search button in BMI tab is function as expected
def test_searchButton():
        # Simulate entering data and clicking the search button
        patient_contact = name_entry.insert(0, "0252525625")
        search_detail_btn.invoke()


        # Verify data insertion
        conn = sqlite3.connect("mass_hospital.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM patients WHERE contact='"+patient_contact+"'")
        cursor.fetchall()

############################################################################
############################################################################
############################################################################
############################################################################

# Testing if retrival of patient's data is function
def test_entryDataTypeByUser():
    weight = "This accepts numeric values not string values"
    height = 10 / 100  # convert height from cm to meters
    bmi = weight / (height * height)
    result_label.config(text="Patient's BMI is {:.1f}".format(bmi))
    if bmi < 18.5:
        status_label.config(text="Underweight", fg="blue")
    elif bmi >= 18.5 and bmi < 25:
        status_label.config(text="Normal weight", fg="green")
    elif bmi >= 25 and bmi < 30:
        status_label.config(text="Overweight", fg="orange")
    else:
        status_label.config(text="Obese", fg="red")

    print(ValueError)

# No validation check for type of data.
def test_noProperValidationChecks():
    name = "Emma Test" # No validation of datatype and the lenght of characters
    email = 'emma@test.com' # No email validation check 
    contact = "0252525625" # No checking of number of characters for a telephone number
    dob =  "02/10/2019" #birthdate_entry.get() # No date vlaidation ckeck
    occupation = "Techer" #occupation_entry.get()

    # Connect to SQLite database
    #conn = sqlite3.connect(":memory:")

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
    





""" def test_insert_data(self):
        # Simulate entering data and clicking the submit button
        self.app.name_entry.insert(0, "John Doe")
        self.app.submit_btn.invoke()

        # Verify data insertion
        self.app.cursor.execute("SELECT * FROM patients")
        result = self.app.cursor.fetchall()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "John Doe") """

"""  def tearDown(self):
        # Close the connection and destroy the app
        self.app.close() """

test_insertingPatientData()
test_retrivalOfPatientData()
test_searchButton()
#test_entryDataTypeByUser()
test_noProperValidationChecks

if __name__ == '__main__':
    unittest.main()


