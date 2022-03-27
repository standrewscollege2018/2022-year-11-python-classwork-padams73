acceptable = ["-", "*"]

name = input("Name:")
status = True
for n in name:
    if n.isalpha():
        pass
    else:
        if n not in acceptable:
            status = False
if status == True:
    print("Accepted")
else:
    print("Rejected")