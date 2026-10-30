n = int(input("Enter number of rows for the hollow diamond: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" + " " * (2 * i - 3) + ("*" if i > 1 else ""))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" + " " * (2 * i - 3) + ("*" if i > 1 else ""))
    