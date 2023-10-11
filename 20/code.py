# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")