# 1) WAP to remove repeated members from a string. print original and resultant string.

# orgStr=input("Enter the original string:")
# resultantString=" "
# for i in orgStr:
#     if i not in resultantString:
#         resultantString += i
# print("Original string is :",orgStr)
# print("Resultant string is :",resultantString)

# 2. WAP deducing multiple string methods.

string1 = input("Enter any string:")
print(f"String is {string1.lstrip()}")
print(f"String is {string1.strip()}")
print(f"String is {string1.rstrip()}")
print(f"String is {string1.find('o')}")
print(f"String is {string1.count('o')}")
print(f"String is {string1.index('o')}")
print(f"String is {string1.replace('Python', 'Java')}")
print(f"String is {string1.split(' ')}")
print(f"String is {string1.startswith('Application')}")
print(f"String is {string1.endswith('Python')}")

