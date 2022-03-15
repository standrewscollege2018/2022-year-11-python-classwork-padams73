# Start a while loop to error-catch the name
# This repeatedly asks for the name until we get a valid name (not blank)
ask_name = True
while ask_name == True:
    name = input("Enter name ")
    # Check if name is blank
    if name == "":
        #If blank, print error message
        print("Error. Re-enter name")
    else:
        # Not blank, so set ask_name to False so we can stop asking
        ask_name = False

# Error catch the age
ask_age = True
while ask_age == True:
    # Check if age entered is an integer
    try:
        age = int(input("Enter age "))
        ask_age = False
    except ValueError:
        # It wasn't an integer, so print an error
        print("Enter an integer")

print(f"{name} is {age} years old")

# Check if school age (<18) or retirement age (>65)
if age < 18:
    print("School age")
elif age > 65:
    print("retirement")
else:
    print("Get to work")