n = int(input("Enter number of passengers: "))

total = 0
for i in range(n):
    age = int(input("Enter age: "))
    distance = int(input("Enter distance in km: "))

    if distance <= 100:
        fare = distance * 2
    elif distance <= 500:
        fare = distance * 1.5
    else:
        fare = distance * 1

    if age < 12:
        fare = fare * 0.5
    elif age >= 60:
        fare = fare * 0.8

    fare = fare + 50
    print("Passenger fare: Rs.", round(fare, 2))
    total = total + fare

print("Total reservation amount: Rs.", round(total, 2))

cancel = input("Cancel reservation? (yes/no): ")

if cancel == "yes":
    penalty = total * 0.20
    print("Cancellation penalty: Rs.", round(penalty, 2))
    print("Refund amount: Rs.", round(total - penalty, 2))