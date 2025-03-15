# 1) Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

 
# try:
#     f =open("demo1.txt","r")
#     content = f.read()
#     print("File content:")
#     print(content)
# except FileNotFoundError:
#     print("File not found error occured because the file that you are trying to open does not exist.")


# 2) Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numeric.


try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = a+b
    print("The sum of", a, "and", b, "is", result)
except TypeError:
    print("Error: Invalid input. Please enter numeric values.")