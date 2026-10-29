budget = float(input("Enter travel budget in Rs: "))
rate = float(input("Enter exchange rate: "))
fee = 0.02
expenses = []

for i in range(3):
    name = input("Enter expense category: ")
    amount = float(input("Enter expense in foreign currency: "))

    cost = amount * rate
    cost = cost + cost * fee
    expenses.append((name, cost))

total = 0
largest = expenses[0]

for item in expenses:
    print(item[0], ": Rs.", round(item[1], 2))
    total = total + item[1]

    if item[1] > largest[1]:
        largest = item

print("Total expenses: Rs.", round(total, 2))
print("Largest expense:", largest[0])

if total <= budget:
    print("Within budget")
else:
    print("Budget exceeded")
