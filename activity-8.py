n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    amount = price * qty

    if amount >= 2000:
        discount = amount * 0.10
    elif amount >= 1000:
        discount = amount * 0.05
    else:
        discount = 0

    if discount > 500:
        discount = 500

    amount = amount - discount

    if name == "food":
        tax = amount * 0.05
    else:
        tax = amount * 0.18

    amount = amount + tax
    print(name, "Final Price: Rs.", round(amount, 2))
    total = total + amount

print("Total Bill: Rs.", round(total, 2))