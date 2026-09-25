##check voting eligibility
age = int(input("enter your age:"))
if age >= 18:
    print(f"you are eligible to vote (age={age})")
else:
    print(f"you are not eligible to vote (age={age})")