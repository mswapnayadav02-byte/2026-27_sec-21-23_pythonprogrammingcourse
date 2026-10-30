n = int(input("Enter a number: "))
temp = n
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10
if sum == temp:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")