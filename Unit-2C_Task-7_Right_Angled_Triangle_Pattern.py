n = int(input("Enter the size of the triangle: "))
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()