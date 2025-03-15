# 1. Write a function in Python to count and display the total number of words in a text file “ABC.txt” and 
# also count uppercase / lowercase character in same  text file

# ABC.txt file content:
# Hii I am Vikash Ramdarash Chaurasiya

# Program:

# def countWordsLowerUpperFile(filename):
#     file=open(filename,"r")
#     countWords=0
#     countLower=0
#     countUpper=0
#     data=file.read()
#     words=data.split()
#     for word in words:
#         countWords+=1
#     print("The total number of words in the file is:",countWords)
#     for char in data:
#         if char.isupper():
#             countUpper+=1
#         else:
#             if char.islower():
#                 countLower+=1
#     print("The total number of lowercase characters in the file is:",countLower)
#     print("The total number of uppercase characters in the file is:",countUpper)
#     file.close()
# countWordsLowerUpperFile("ABC.txt")

# Output:
# The total number of words in the file is: 6
# The total number of lowercase characters in the file is: 26
# The total number of uppercase characters in the file is: 5

# 2. Write a function display_words() in python to read lines from a text file "story.txt",
# and display those words, which are less than 4 characters.

# story.txt file content:
# Hii this is a very big story

# Program:

def display_words():
    file=open("story.txt","r")
    data=file.read()
    words=data.split()
    for i in words:
        if len(i)<4:
            print(i)
    file.close()
display_words()

# Output:
# Hii
# is
# a
# big