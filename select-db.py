# Import the SQLite library
import sqlite3

# Set the database to connect to
DATABASE = 'student.db'

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Select information from the student table
cursor.execute("SELECT first_name, last_name, tutor FROM student WHERE age <18")
results = cursor.fetchall()

number_of_results = len(results)
print(f"{number_of_results} result(s) found")

# Display results down the page
for result in results:
    #print(result)
    print(f"{result[0]:10} {result[1]:15} {result[2]:3}")

    
    
