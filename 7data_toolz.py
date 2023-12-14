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
        return None
    
# Function to extract a column
def extract_column(column_index, data):
    try:
        column_values = [row[column_index] for row in data]
        return column_values
    except (ValueError, IndexError) as e:
        return None    
    
def remove_header(data):
    try:
        data = data[1:]
        return data
    except IndexError as e:
        return None

def convert_to_float(data):
    try:
        converted_data =  [float(item) for item in data] 
        return converted_data
    except ValueError as e:
        return None
    
# Function to calculate average
def calculate_average(column_values):
    try:
        average = sum(column_values) / len(column_values)
        return average
    except ZeroDivisionError as e:
        return None    

extract_column_index = curry(extract_column)
extract_score = extract_column_index(1)
extract_name = extract_column_index(0)

data = read_csv_file('example.csv')    

names = pipe(
    data, 
    extract_name, 
    remove_header
)

average_result = pipe(
    data, 
    extract_score, 
    remove_header, 
    convert_to_float, 
    calculate_average
)

print(f"An average score of {', '.join(names[:-1])} and {names[-1]} is {average_result}")