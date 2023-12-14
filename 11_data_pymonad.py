import csv
import os
from pymonad.tools import curry
from pymonad.either import Left, Right

# Function to handle file reading
def read_csv_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as csvfile:
            return Right(list(map(list, csv.reader(csvfile))))
    else:
        return Left("Error: File not found")

def remove_header(data):
    return Right(data[1:]) if len(data) > 1 else Left("Error: Unable to remove header")

@curry(2)
def extract_column(column_index, data):
    return (
        Right(list(map(lambda row: row[column_index], data))) 
        if len(data) > column_index
        else Left("Error: Unable to extract column")  
    )

def convert_to_float(data):
    try:
        converted_data =  [float(item) for item in data] 
        return Right(converted_data)
    except ValueError as e:
        return Left("Error: Unable to convert to float")

def calculate_average(column_values):
    return ( 
        Right(sum(column_values) / len(column_values))
        if len(column_values) > 0
        else Left("Error: Division by zero")   
    )

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
