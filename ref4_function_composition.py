import csv
from pymonad.tools import curry
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
    # print(f"remove_header: {data}")
    try:
        data = data[1:]
        return data
    except IndexError as e:
        return None

@curry(2)
def extract_column(column_index, data):
    try:
        column_values = [row[column_index] for row in data]
        return column_values
    except (ValueError, IndexError) as e:
        return None

def convert_to_float(data):
    converted_data = [float(item) for item in data]
    return converted_data

def calculate_average(column_values):
    if column_values is None or not column_values:
        return None, "Cannot calculate average due to empty or missing column"
    try:
        average = sum(column_values) / len(column_values)
        return average
    except ZeroDivisionError as e:
        return None

def compose(*functions):
    def composed_function(x):
        result = x
        for func in functions:
            result = func(result)
        return result
    return composed_function

# Data pipeline using function composition
csv_file_path = 'example.csv'
SCORE_COLUMN_INDEX: Final[int] = 1
extract_score_columns = extract_column(SCORE_COLUMN_INDEX)  

data_pipeline = compose(
    read_csv_file , 
    remove_header,
    extract_score_columns,
    convert_to_float,
    calculate_average
)

# all_data = read_csv_file(csv_file_path)
result = data_pipeline(csv_file_path)

if result is not None:
    print(f"An average score of this class is {result}")
else:
    print("Error processing data")
