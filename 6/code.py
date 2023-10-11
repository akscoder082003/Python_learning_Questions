# Write a python program that accepts a filename from the user and prins the extension of the file. 

filename = input("Enter the filename: ")
file_extension = filename.split(".")
print("The extension of the file is : " + repr(file_extension[-1]))