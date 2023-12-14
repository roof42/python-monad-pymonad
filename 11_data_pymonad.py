import csv
from typing import Final
from pymonad.tools import curry
from pymonad.either import Left, Right

# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]
            return Right(data)
    except FileNotFoundError as e:
        return Left("Error: File not found")

def remove_header(data):
    return Right(data[1:]) if len(data) > 1 else Left("Error: Unable to remove header")

@curry(2)
def extract_column(column_index, data):
    if data is None or not data:
        return Left("Error: Cannot calculate average due to empty or missing column")    
    try:
        column_values = [row[column_index] for row in data]
        return Right(column_values)
    except (ValueError, IndexError) as e:
        return Left("Error: Unable to extract column")

extract_score_column = extract_column(1)
extract_name_column = extract_column(0)

def convert_to_float(data):
    right = Right([float(item) for item in data])
    left = Left("Error: Unable to convert to float")
    return right if data else left

def calculate_average(column_values):
    right = Right(sum(column_values) / len(column_values))
    left = Left("Error: Division by zero during average calculation")
    return  right if column_values else left

# Data pipeline using the Either monad and custom sequencing operator
csv_file_path = 'example.csv'

data =  read_csv_file(csv_file_path)
names = (data
    .then (remove_header)
    .then (extract_name_column)
)

result = (
    data
    .then (remove_header)
    .then (extract_score_column)
    .then (convert_to_float)
    .then (calculate_average) 
)


if result.is_right and names.is_right:
    print(f"An average score of {', '.join(names.value[:-1])} and {names.value[-1]} is {result.value}")
else:   
    print(f"Error processing data: {result.value}")
