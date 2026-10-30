n = int(input("Enter the value of n: "))
largest = float('-inf')
for _ in range(n):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num
print(f"The largest number is: {largest}")
