# This code works perfectly for success path. 
# It will break in the middel of execution if there is something wrong
# Lets move to the next section that we will handle exception in a proper way
import csv
from toolz import curry, pipe
from typing import Final

# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            return [row for row in csv.reader(csvfile)]
    except FileNotFoundError as e:
        return None

# Extract 3 functions that do one thing and do it well
@curry 
def extract_column(column_index, data):
    try:
        return [row[column_index] for row in data]
    except (ValueError, IndexError) as e:
        return None    

@curry 
def remove_row(row_index, data):
    try:
        return data[row_index:]
    except IndexError as e:
        return None

@curry 
def convert_to(converter, data):
    try:
        return [converter(item) for item in data] 
    except ValueError as e:
        return None

# Function to calculate average
def calculate_average(column_values):
    try:
        return sum(column_values) / len(column_values)
    except ZeroDivisionError as e:
        return None

# Data pipeline
csv_file_path = 'example.csv'
score_column_index  = 1
header_row_index = 1
score_column    = extract_column(score_column_index)
removed_header  = remove_row(header_row_index)
score_as_float  = convert_to(float)

average_result = pipe(
    read_csv_file(csv_file_path), 
    score_column, 
    removed_header, 
    score_as_float, 
    calculate_average
)

print(f"An average score is {average_result}")