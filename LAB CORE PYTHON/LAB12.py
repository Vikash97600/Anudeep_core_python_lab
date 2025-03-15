# 1.WAP to create a tuple and append another tuple to it get the count of total members & repeated members
# similarly print length of this new tuple

# tuple1=(11,12,13)
# tuple2=(14,15,16)
# new_tuple=(tuple1+tuple2)

# print(f"Appended tuple is : {new_tuple}.")

# count = len(new_tuple)
# print(f"Total member of the 'new_tuple' is  : {count}")     

# unique=[]
# list1=list(new_tuple)
# for i in list1:
#     if i not in unique:
#         unique.append(i)
# repeated=False
# for j in unique:
#     unique_count=0
#     for k in list1:
#         if (j==k):
#             unique_count+=1
#     if(unique_count>=2):
#         print(f"The word '{j}' is repeated  {unique_count} times")
#         repeated = True
# if(repeated==False):
#     print("No members are repeated.")


# 2. WAP to deduce use of sorting in tuples.

tuple1=(1,3,2,4,6,5,8,7)
ascendingOreder=sorted(tuple1)
descendingOrder=ascendingOreder[::-1]
print("The Sorted form of tuple (ascending order) is: ",tuple(ascendingOreder) )
print("The Sorted form of tuple (descending order) is: ",tuple(descendingOrder))
print("The reversed form of tuple1 is: ",tuple1[::-1] )




























