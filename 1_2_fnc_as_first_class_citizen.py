import csv
# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            return [row for row in csv.reader(csvfile)]
    except FileNotFoundError as e:
        return None

# Extract 3 functions that do one thing and do it well
def extract_column(column_index, data):
    try:
        return [row[column_index] for row in data]
    except (ValueError, IndexError) as e:
        return None    

def remove_row(row_index, data):
    try:
        return data[row_index:]
    except IndexError as e:
        return None

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
score_column_index = 1
header_row_index = 1
data = read_csv_file(csv_file_path)

if data == None:
    print("Error reading CSV file")
else:
    score_column_values     = extract_column(score_column_index, data)
    removed_header_data     = remove_row(header_row_index, score_column_values)
    score_column_as_float   = convert_to(float, removed_header_data)

    if score_column_as_float == None:
        print("Error extracting column")
    else:
        result = calculate_average(score_column_as_float)
        if result == None:
            print("Error calculating average")
        else:
            print(f"The average is: {result}")