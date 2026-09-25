##find the largest of three numbers using nested if statements
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if a > b:
    if a > c:
        print(f"{a} is the largest")
    else:
        print(f"{c} is the largest")
else:
    if b > c:
        print(f"{b} is the largest")
    else:
        print(f"{c} is the largest")