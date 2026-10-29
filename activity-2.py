bills = []

for month in range(1, 4):
    units = int(input("Enter units for month " + str(month) + ": "))

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    elif units <= 300:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5
    else:
        bill = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7

    bill = bill + 100  # Fixed charge

    if bill > 2000:
        bill = bill + bill * 0.05  # 5% surcharge
    elif bill < 500:
        bill = bill - bill * 0.10  # 10% rebate

    bills.append(bill)
    print("Month", month, "Bill: Rs.", round(bill, 2))

for i in range(1, 3):
    if bills[i] > bills[i - 1] * 1.5:
        print("Unusual increase in month", i + 1)

print("Total bill for 3 months: Rs.", round(sum(bills), 2))