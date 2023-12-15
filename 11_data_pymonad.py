import csv
import os
from pymonad.tools import curry
from pymonad.either import Left, Right

def read_csv_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as csvfile:
            return Right(list(map(list, csv.reader(csvfile))))
    else:
        return Left("Error: File not found")

def remove_header(data):
    if len(data) > 1:
        return Right(data[1:])  
    else: 
        return Left("Error: Unable to remove header")

@curry(2)
def extract_column(column_index, data): 
    if len(data) > column_index:
        return Right(list(map(lambda row: row[column_index], data)))
    else: 
        return Left("Error: Unable to extract column")  

def convert_to_float(data):
    converted_data = [float(item) if item.isdigit() else None for item in data]
    if all(x is not None for x in converted_data):
        return Right(converted_data)
    else:
        return Left("Error: Unable to convert to float")    

def calculate_average(column_values):
    if len(column_values) > 0:
        return Right(sum(column_values) / len(column_values))
    else: 
        return Left("Error: Division by zero")   

# Data pipeline using the Either monad and custom sequencing operator
csv_file_path = 'example.csv'
score_column_index = 1

result = (
    read_csv_file(csv_file_path)
    .then (remove_header)
    .then (extract_column(score_column_index))
    .then (convert_to_float)
    .then (calculate_average) 
)

if result.is_right():
    print(f"An average score is {result}")
else:   
    print(f"Error processing data: {result}")
