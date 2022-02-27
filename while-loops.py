# Boolean variable
keep_asking = True
while keep_asking == True:
    name = input("Name?")
    if name == "stop":
        keep_asking = False
    else:
        print(f"Hello {name}")