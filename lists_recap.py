# Set up empty list to store cars
cars = []

# Start asking for cars
ask_car = True
while ask_car == True:
    car = input("Enter name of car: ")
    # If user enters end, stop asking
    if car == "end":
        ask_car = False
    else:
        # Otherwise, add the car to the list
        cars.append(car)
        # Print the list so we can see it changing
        print(cars)

# Print out the first item in the list
print(cars[0])

# Print out the list down the page using a for loop
for c in cars:
    print(c)

# Print numbered list so user can choose a car
#Get number of cars
length = len(cars)

for i in range(length):
    print(f"{i+1} {cars[i]}")