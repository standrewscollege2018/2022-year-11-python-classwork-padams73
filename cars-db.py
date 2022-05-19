# Import the SQLite library
import sqlite3

# Set the database to connect to
DATABASE = 'cars.db'

# Connect to the database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()
'''
# Query 1: Select all info from the car table
results = cursor.execute("SELECT * FROM car")


print("Welcome to the cars database")
ask = True
while ask:
    plate = input("Enter number plate: ")
    if plate == "":
        print("Plate cannot be blank")
    else:
        ask = False
    
        
query = f"SELECT * FROM car WHERE number_plate LIKE '%{plate}%'"
print(query)
cursor.execute(query)
results = cursor.fetchall()

#print(f"{len(results)} result(s) found")
if len(results)>0:
    print(f"{'ID':3} {'Plate':6} {'Colour':10} {'Driver':15} {'Make':10} {'Model':12}")
    print("="*56)
    for result in results:
        print(f"{result[0]:3} {result[1]:6} {result[2]:10} {result[3]:15} {result[4]:10} {result[5]:12}")
else:
    print("No records found")


    
    
