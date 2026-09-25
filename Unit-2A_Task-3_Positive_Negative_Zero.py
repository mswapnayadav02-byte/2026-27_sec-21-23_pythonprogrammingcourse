##check if a number is positive, negative, or zero
num = float(input("enter a number:"))
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")