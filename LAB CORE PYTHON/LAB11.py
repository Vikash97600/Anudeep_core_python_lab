# 1.Write a Python program to get the key, value and item in a dictionary.
# input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key and their corresponding values are:")
for key, value in dict_num.items():
    print(key,':', value)
print(f"The items in the dictionary are:{dict_num.items()}")

# 2. Write a Python program to deduce use of multiple dictionary functions.

# num={1:11,2:22,3:33,4:44,5:55,6:66,7:77,8:88,9:99,10:100}
# print(f"The itens of the dictionary are:{num.items()}")

# print("Print Keys only:")
# for key in num.keys():
#     print(key)


# print("Values only:")
# for value in num.values():
#     print(value)

# print("Update dictionary:")
# (num.update({1:111}))
# print(num)

# print("Delete a key value from dictionary:")
# del num[1]

# print("Length of dictionary:")
# print(len(num))

# print("Copy dictionary:")
# secondNewDictionary=num.copy()
# print(secondNewDictionary)

# print("Convert thr dictionary to string:")
# print(str(num))

# print("Convert the dictionary to list:")
# print(list(num))

# print("Convert the dictionary to tuple:")
# print(tuple(num))

# print("Convert the dictionary to set:")
# print(set(num))

# print("Remove the element from dictionary:")
# num.pop(2)
# print(num)

# print("Remove the last element from dictionary:")
# num.popitem()
# print(num)

# print("Clear/empty the dictionary:")
# num.clear()
# print(num)

