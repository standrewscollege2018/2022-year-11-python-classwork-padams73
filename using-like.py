# Import the SQLite library
import sqlite3

# Set the database to connect to
DATABASE = 'student.db'

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()


search = input("Enter name to search on: ")
search = "%"+search+"%"

cursor.execute("SELECT * FROM student WHERE first_name LIKE ?", (search,))
search_results = cursor.fetchall()   

for s in search_results:
    print(s)
