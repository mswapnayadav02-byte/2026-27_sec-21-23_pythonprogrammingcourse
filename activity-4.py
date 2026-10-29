venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per participant: "))

sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per participant: "))

total = venue + equipment + catering + transport
remaining = total - sponsorship

if remaining < 0:
    remaining = 0

if fee > certificate:
    count = int(remaining / (fee - certificate)) + 1
else:
    count = 0

print("Total Event Cost:", total)
print("Sponsorship Shortfall:", max(0, total - sponsorship))
print("Minimum Participants Needed:", count)
participants = int(input("Enter expected participants: "))
income = sponsorship + participants * fee
cost = total + participants * certificate

print("Total Income:", income)
print("Total Cost:", cost)

if income >= cost:
    print("Event is financially successful")
else:
    print("More funds are required")