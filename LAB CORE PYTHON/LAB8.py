# 1. WAP to print count of uppercase, lowercase, numbers and special characters in a string.
# print count seperately.

# string = input("Enter any string:")

# upper, lower, digit, splChar = 0, 0, 0, 0
# for char in string:
#     if char.isupper():
#         upper += 1
#     elif char.islower():
#         lower += 1
#     elif char.isdigit():
#         digit += 1
#     else:
#         splChar += 1

# print(f"Number of Uppercase letters present in {string} is {upper}")
# print(f"Number of Lowercase letters present in {string} is {lower}")
# print(f"Number of Digits present in {string} is {digit}")
# print(f"Number of Special Characters present in {string} is {splChar}")

# 2. WAP with several string methods.

str = input("Enter any string:")
print(f"Length of string is {len(str)}")
print(f"String is {str.lower()}")
print(f"String is {str.upper()}")
print(f"String is {str.swapcase()}")
print(f"String is {str.title()}")
print(f"String is {str.capitalize()}")
print(f"String is {str.center(50)}")
print(f"String is {str.ljust(50)}")



