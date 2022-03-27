# Import the SQLite library
import sqlite3

# Set the database to connect to
DATABASE = 'student.db'

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Get information about the student to be added
print("Please enter the information about the new student")
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))
year = int(input("Year level: "))
tutor = input("Tutor group: ")
phone = input("Phone: ")


# Run the query to insert the record
cursor.execute("INSERT INTO student (first_name, last_name, age, year_group, tutor, phone) VALUES (?,?,?,?,?,?)",(first_name, last_name, age, year, tutor, phone))

connection.commit()

# Select information from the student table
cursor.execute("SELECT first_name, last_name, tutor FROM student")
results = cursor.fetchall()

number_of_results = len(results)
print(f"{number_of_results} result(s) found")

# Display results down the page
for result in results:
    #print(result)
    print(f"{result[0]:10} {result[1]:15} {result[2]:3}")

    
    
