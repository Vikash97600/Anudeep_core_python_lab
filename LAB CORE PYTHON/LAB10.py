# 1. Write a Python program to get the largest and smallest number from a list without using built-in functions. 

# list=[1,2,3,4,5,6,7,8,9,10]
# largest=list[0]
# smallest=list[0]
# for i in list:
#     if i>largest:
#         largest=i
#     if i<smallest:
#         smallest=i

# print("Largest number is:",largest)
# print("Smallest number is:",smallest)





# 2. Write a Python program to find duplicate values from a list and display those.

list1=[1,2,3,4,5,1,7,8,9,0]
duplicatesValues=[]
for i in list1:
    if list1.count(i)>1:
        if i not in duplicatesValues:
            duplicatesValues.append(i)
if duplicatesValues==[]:
    print("There are no duplicate values in the list")
else:
    print("Duplicate values are:",duplicatesValues)


