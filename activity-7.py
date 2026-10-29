plans = [(199, 2, 28), (299, 3, 56), (399, 5, 84)]

usage = float(input("Enter data usage (GB): "))
days = int(input("Enter validity needed (days): "))
budget = float(input("Enter your budget: "))

best = -1

for price, data, validity in plans:
    if usage <= data and days <= validity and price <= budget:
        if best == -1 or price < best:
            best = price

if best == -1:
    print("No suitable plan available")
else:
    print("Most economical plan: Rs.", best)
