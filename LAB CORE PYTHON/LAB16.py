# 1. Write a Python script to read a CSV file with missing values and replace the
# missing values with a default value (e.g., "Unknown" or 0).
# Sample Data (missing_data.csv):

# Name, Age, City
# Alice, , New York
# Bob, 25,
# Charlie, 35, Chicago

# Program:


# import csv

# def handleCsvValues(inputFile, defaultValue):
#     with open(inputFile, mode='r') as file:
#         reader = csv.reader(file)
#         rows=[row for row in reader]
#         updated_rows=[]
#         for row in rows:
#             updated_row=[value if value !=' 'else defaultValue for value in row]       
#             updated_rows.append(updated_row)
#             print(updated_row)


    
# handleCsvValues('missing_data.csv','unknown')


# 2. Write a Python script to validate JSON data by checking if it contains required
# fields and if the data types are correct (e.g., integers for IDs, strings for names).
# Sample Data (data.json):
# [
# {
# "Product ID": 101,
# "Name": "Widget A",
# "Price": 25.50
# },
# {
# "Product ID": "102",
# "Name": "Widget B",
# "Price": "40.00"
# }
# ]

# Program:

import json

def readJsonData(file_path):
    with open(file_path,"r") as file:
        data=json.load(file)
    for item in data:
        if not isinstance(item.get('Product ID'),int):
            print("Product ID must be integer")
        if not isinstance(item.get('Name'),str):
            print("Name must be string")
        if not isinstance(item.get('Price'),float):
            print("Price must be float")

readJsonData('data.json')
