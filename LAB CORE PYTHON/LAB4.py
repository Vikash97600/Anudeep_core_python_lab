# 1. Accept a name from the user and display that in lower case using lower() function


# def nameConvertLower(x):
#     nameLower=x.lower()
#     print(nameLower)
# name=input("Enter your name:")
# nameConvertLower(name)


# 2. Write a function that takes one argument and returns 'Positive' if the number is greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0. 
# Test it with different numbers

def checkNum(num):
    if num>0:
        print("Positive")
    elif num<0:
        print("Negative")
    else:
        print("Zero")
num=int(input("Enter the number to check :"))
checkNum(num)