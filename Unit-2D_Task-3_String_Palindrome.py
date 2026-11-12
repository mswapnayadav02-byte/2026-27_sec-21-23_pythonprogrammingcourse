# String Palindrome

n = input("Enter a string: ")

reverse = n[::-1]

if n == reverse:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")