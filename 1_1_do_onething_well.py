import csv
# Function to handle file reading
def read_csv_file(file_path):
    with open(file_path, 'r') as csvfile:
        return [row for row in csv.reader(csvfile)]

# Extract 3 functions that do one thing and do it well
def extract_score_column(data):
    return None

def remove_header(data):
    return None

def convert_score_float(data):
    return None

# Function to calculate average
def calculate_average(column_values):
    return sum(column_values) / len(column_values)

# Data pipeline
csv_file_path = 'example.csv'
score_column_index = 1
header_row_index = 1

data = read_csv_file(csv_file_path)
if data == None:
    print("Error reading CSV file")
else:
    score_column_values     = extract_score_column(data)
    removed_header_data     = remove_header(score_column_values)
    score_column_as_float   = convert_score_float(removed_header_data)
    if score_column_as_float == None:
        print("Error extracting column")
    else:
        result = calculate_average(score_column_as_float)
        if result == None:
            print("Error calculating average")
        else:
            print(f"The average is: {result}")