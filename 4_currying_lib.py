from pymonad.tools import curry
import csv
from typing import Final

# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]
            return data
    except FileNotFoundError as e:
        return None

def remove_header(data):
    try:
        data = data[1:]
        return data
    except IndexError as e:
        return None

# Curried function to extract a column
@curry(2)
def extract_column(column_index, data):
    try:
        column_values = [row[column_index] for row in data]
        return column_values
    except (ValueError, IndexError) as e:
        return None

SCORE_COLUMN_INDEX: Final[int] = 1
NAME_COLUMN_INDEX: Final[int]  = 0
extract_score_columns = extract_column(SCORE_COLUMN_INDEX)
extract_name_columns = extract_column(NAME_COLUMN_INDEX)

def convert_to_float(data):
    converted_data =  [float(item) for item in data] 
    return converted_data

# Function to calculate average
def calculate_average(column_values):
    if column_values is None or not column_values:
        return None, "Cannot calculate average due to empty or missing column"
    try:
        average = sum(column_values) / len(column_values)
        return average
    except ZeroDivisionError as e:
        return None

# Data pipeline
csv_file_path = 'example.csv'
# Step 1: Read CSV file
all_data = read_csv_file(csv_file_path)

if all_data == None:
    print("Error reading CSV file")
else:
    data_with_no_header = remove_header(all_data)
    score_column = extract_score_columns(data_with_no_header)
    name_column = extract_name_columns(data_with_no_header)
    scores = convert_to_float(score_column)
    result = calculate_average(scores)
    print(f"An average score of {name_column} is {result}")