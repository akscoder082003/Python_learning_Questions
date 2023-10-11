# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers. 

data = input("Enter the comma seperated numbers: ")
list = data.split(",")
tuple = tuple(list)
print("List: ",list)
print("Tuple: ",tuple)