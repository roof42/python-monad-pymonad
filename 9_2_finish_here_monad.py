import csv
import os
from pymonad.tools import curry
from pymonad.either import Left, Right

def read_csv_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as csvfile:
            return Right([row for row in csv.reader(csvfile)])
    else:
        return Left("Error: File not found")

@curry(2)
def remove_row(row_index, data):
    if len(data) > 1:
        return Right(data[row_index:])  
    else: 
        return Left("Error: Unable to remove header")

@curry(2)
def extract_column(column_index, data): 
    if len(data) > column_index:
        return Right([row[column_index] for row in data])
    else: 
        return Left("Error: Unable to extract column")  

@curry(2)
def convert_to(converter, data):
    converted_data = [converter(item) if item.isdigit() else None for item in data]
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
header_row_index = 1
# Partial apply
remove_header = remove_row(header_row_index)
extract_score_column = extract_column(score_column_index)
convert_score_to_float = convert_to(float)

result = (
    read_csv_file(csv_file_path)
    .then (extract_score_column)
    .then (remove_header)
    .then (convert_score_to_float)
    .then (calculate_average) 
)

if result.is_right():
    print(f"An average score is {result}")
else:   
    print(f"Error processing data: {result}")
