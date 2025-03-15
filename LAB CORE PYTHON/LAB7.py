# 1. Python program to check if the given string is a palindrome 

def palindrome(str):
    if str==str[::-1]:
        print(f"The string {str} is palindrome")
    else:
        print(f"The string {str} is not palindrome")

a=input("Enter the string:")
palindrome(a)

# 2. Python program to check if a given number is an Armstrong number

# def armstrong(num):
#     temp=num
#     sum=0
#     while num>0:
#         rem=num%10
#         sum=sum+rem*rem*rem
#         num=num//10

#     if temp==sum:
#         print(f"The number {temp} is armstrong")
#     else:
#         print(f"The number {temp} is not armstrong")

# a=int(input("Enter the value of a:"))
# armstrong(a)