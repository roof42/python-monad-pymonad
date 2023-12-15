import csv
from toolz import curry, pipe

# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]
            return data
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error reading file: {e}")

# Function to extract a column
def extract_column(column_index, data):
    try:
        column_values = [row[column_index] for row in data]
        return column_values
    except (ValueError, IndexError) as e:
        raise ValueError(f"Error extracting column: {e}")

def remove_header(data):
    try:
        data = data[1:]
        return data
    except IndexError as e:
        raise IndexError(f"Error removing header: {e}")

def convert_to_float(data):
    try:
        converted_data = [float(item) for item in data]
        return converted_data
    except ValueError as e:
        raise ValueError(f"Error converting to float: {e}")

# Function to calculate average
def calculate_average(column_values):
    try:
        average = sum(column_values) / len(column_values)
        return average
    except ZeroDivisionError as e:
        raise ZeroDivisionError("Error calculating average: Division by zero")

extract_column_index = curry(extract_column)
extract_score = extract_column_index(1)
extract_name = extract_column_index(0)

try:
    average_result = pipe(
            read_csv_file('example.csv'),
            extract_score,
            remove_header,
            convert_to_float,
            calculate_average
    )
    print(f"An average score is {average_result}")
except (FileNotFoundError, ValueError, IndexError, ZeroDivisionError) as e:
    print(f"Exception caught: {e}")
