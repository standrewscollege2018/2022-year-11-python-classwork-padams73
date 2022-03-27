# Import the SQLite library
import sqlite3

# Set the database to connect to
DATABASE = 'student.db'

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Select names from the student table
cursor.execute("SELECT student_id, first_name, last_name FROM student")
results = cursor.fetchall()


# Display names down the page
for result in results:
    name = f"{result[1]} {result[2]}"
    print(f"{result[0]:3} {name}")

# Get number of student to display
selection = int(input("Enter number: "))

cursor.execute("SELECT * FROM student WHERE student_id = ?", (selection,))
details = cursor.fetchall()

for detail in details:
    print(f"Name: {detail[1]} {detail[2]}")
    print(f"Tutor group: {detail[5]}")
    print(f"Age: {detail[3]}")
    print(f"Year: {detail[4]}")
    print(f"Phone: {detail[6]}")




