''' This program demonstrates how to connect to a database using Python,
and also how to run a query and display the results '''

# import the sqlite3 library
import sqlite3

# Set the database to connect to
DATABASE = 'student.db'

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Run a query
cursor.execute("SELECT * FROM student WHERE tutor='GON'")
students = cursor.fetchall()

# Loop through the results and display
for student in students:
    name = f"{student[1]} {student[2]}"
    print(f"{name:22} {student[5]:3}")




