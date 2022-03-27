# Import the SQLite library
import sqlite3

# Set the database to connect to
DATABASE = 'student.db'

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Get the first letter of the last name
letter = input("Enter first letter of last name: ")
letter = letter+"%"

# Get the age range
age = int(input("Enter min age: "))

# Select names from the student table
cursor.execute("SELECT first_name, last_name, age FROM student WHERE age > ? AND last_name LIKE ?", (age, letter))
results = cursor.fetchall()


# Display results down the page
for result in results:
    #print(result)
    print(f"{result[0]:10} {result[1]:15} {result[2]:3}")




