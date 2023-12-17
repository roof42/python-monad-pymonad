import csv
from toolz import curry, pipe
from typing import Final

# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            return [row for row in csv.reader(csvfile)]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error reading file: {e}")

# Extract 3 functions that do one thing and do it well
@curry 
def extract_column(column_index, data):
    try:
        return [row[column_index] for row in data]
    except (IndexError) as e:
        raise IndexError(f"Error extracting column: {e}")

@curry 
def remove_row(row_index, data):
    try:
        return data[row_index:]
    except IndexError as e:
       raise IndexError(f"Error removing header: {e}")

@curry 
def convert_to(converter, data):
    try:
        return [converter(item) for item in data] 
    except ValueError as e:
        raise ValueError(f"Error converting to float: {e}")

# Function to calculate average
def calculate_average(column_values):
    try:
        return sum(column_values) / len(column_values)
    except ZeroDivisionError as e:
        raise ZeroDivisionError(f"Error zero division: {e}")

#============== Data pipeline ================================
csv_file_path = 'example.csv'
score_column_index  = 1
header_row_index = 1
score_column    = extract_column(score_column_index)
remove_header  = remove_row(header_row_index)
convert_score_to_float  = convert_to(float)

try:
    average_result = pipe(
        read_csv_file(csv_file_path), 
        score_column, 
        remove_header, 
        convert_score_to_float, 
        calculate_average
    )
    print(f"An average score is {average_result}")
except (FileNotFoundError, ValueError, IndexError, ZeroDivisionError) as e:
    print(f"Exception caught: {e}")

#It work, however toolz didn't provide us the way to hanle exception in functional style
#We need 