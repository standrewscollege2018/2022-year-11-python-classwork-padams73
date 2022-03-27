# Import the SQLite library
import sqlite3

# Set the database to connect to
DATABASE = 'titanic.db'

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Get the travel class
travel_class = input("What class do you want to search on? (1-3)")

# Get whether they are survivors or victims
survived = int(input("Enter 1 for list of survivors or 0 for deceased: "))

# Select names
cursor.execute("SELECT name FROM titanic WHERE class = ? AND survived = ?", (travel_class, survived))
results = cursor.fetchall()
total = len(results)

# Display results down the page
print(f"There are {total} results found")
for result in results:
    #print(result)
    print(f"{result[0]}")




