
consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges!")
else:
    total = consultation + diagnostic + treatment

    if total > 5000:
        concession = total * 0.10
    else:
        concession = 0

    final_bill = total - concession

    if final_bill < 2000:
        category = "Low Payment"
    elif final_bill <= 5000:
        category = "Medium Payment"
    else:
        category = "High Payment"

    print("Total Bill: Rs.", total)
    print("Concession: Rs.", concession)
    print("Final Bill: Rs.", final_bill)
    print("Patient Category:", category)
