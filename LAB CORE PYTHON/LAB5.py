# 1. Write a python program to reverse a number using a while loop.

def reverse(num):
    temp=num
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print(rev)
a=int(input("Enter the value of a:"))
reverse(a)

# 2. Write a python program to check whether a number is palindrome or not?

# def palindrome(num):
#     temp=num
#     rev=0
#     while num>0:
#         rem=num%10
#         rev=rev*10+rem
#         num=num//10

#     if temp==rev:
#         print(f"The number {temp} is palindrome")
#     else:
#         print(f"The number {temp} is not palindrome")

# a=int(input("Enter the value of a:"))
# palindrome(a)