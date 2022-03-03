names = ["John", "Lexi", "Sam", "asdasdasdasd"]
ages = [16, 15, 16, 200]
eyes = ["Brown", "Blue", "Hazel", "asd"]

length = len(names)
for i in range(length):
    print(f"{names[i]} is {ages[i]} years old and has {eyes[i]} eyes")

print(f"{'Country':15} {'Ages':10} {'Eyes':10}")
print("=" * 35)
for i in range(length):
    print(f"{names[i]:<15} {ages[i] :<10} {eyes[i] :<10}")