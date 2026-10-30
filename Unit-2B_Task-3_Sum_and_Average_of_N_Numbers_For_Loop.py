n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n + 1):
    sum += i
average = sum / n if n > 0 else 0
print(f"Sum: {sum}")
print(f"Average: {average}")

