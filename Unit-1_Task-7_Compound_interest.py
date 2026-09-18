principal = float(input("Enter principal:"))
rate = float(input("Enter rate:")) 
time = float(input("Enter time:"))
amount = principal * (1+ rate / 100) ** time
compound_interest = amount - principal - amount
print("compound interest=",compound_interest)