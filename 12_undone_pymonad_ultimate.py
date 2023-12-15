import csv
import os
from typing import Final
from pymonad.tools import curry
from pymonad.either import Left, Right

# Function to handle file reading
def read_csv_file(file_path):
    with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]
            return data
    return IO(read_file)

def remove_header(data):
    return (
        Right(data[1:]) 
        if len(data) > 1 
        else Left("Error: Unable to remove header")
    )

@curry(2)
def extract_column(column_index, data):
    return (
        Right(data).bind(lambda rows: 
        Right(list(map(lambda row: row[column_index], rows))))
    )

extract_score_column = extract_column(1)
extract_name_column = extract_column(0)

def convert_to_float(data):
    return (
        Right(list(map(float, data))) 
        if data 
        else Left("Error: Unable to convert to float")
    )


def calculate_average(column_values):
    return  (
        Right(sum(column_values) / len(column_values)) 
        if column_values 
        else Left("Error: Division by zero")
    )

# Data pipeline using the Either monad and custom sequencing operator
csv_file_path = '1example.csv'

# data =  read_csv_file(csv_file_path)

names = (
    read_csv_file(csv_file_path)
    .then (remove_header)
    .then (extract_name_column)
)

result = (
    read_csv_file(csv_file_path)
    .then (remove_header)
    .then (extract_score_column)
    .then (convert_to_float)
    .then (calculate_average) 
)


if result.is_right and names.is_right:
    print(f"An average score of {', '.join(names.value[:-1])} and {names.value[-1]} is {result.value}")
else:   
    print(f"Error processing data: {result.value}")
