# Import the SQLite library
import sqlite3

# Set the database to connect to
DATABASE = 'titanic.db'

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Welcome and explanation
print("Welcome to the Titanic passengers database")
print("==========================================")
print("Here you can search for passengers and their details\n")

# Get the name to search for
name = input("Enter the name: ")
name = "%"+name+"%"

# Select names
cursor.execute("SELECT * FROM titanic WHERE name LIKE ?", (name,))
results = cursor.fetchall()
total = len(results)

# Display results down the page
print(f"{total} result(s) found")
print()
print(f"{'Name':40} {'Class':^5} {'Age':^3} {'Fare':>6} {'Status':<8}")
print("="*65)
if total > 0:
    for result in results:
        if result[1]==1:
            status = "Survived"
        else:
            status = "Deceased"
        print(f"{result[3]:40} {result[2]:^5} {result[5]:^3} {result[8]:>6} {status:<8}")
    




