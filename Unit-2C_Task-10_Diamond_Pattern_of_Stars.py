n = int(input("Enter the size of the diamond: "))
#upper half of the diamond
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
    #lower half of the diamond
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()