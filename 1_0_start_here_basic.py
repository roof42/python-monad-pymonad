import csv

# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]
            return data
    except FileNotFoundError as e:
        return None

# Function to extract a colum
def extract_column(column_index, data):
    try:
        column_values = [float(row[column_index]) for row in data[1:]]
        return column_values
    except (ValueError, IndexError) as e:
        return None

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
column_index = 1  # Assuming the second column (index 1) needs to be processed

# Step 1: Read CSV file
data = read_csv_file(csv_file_path)

if data == None:
    print("Error reading CSV file")
else:
    # Step 2: Extract column
    score_column_values = extract_column(column_index, data)
    if score_column_values == None:
        print("Error extracting column")
    else:
        # Step 3: Calculate average
        result = calculate_average(score_column_values)

        if result == None:
            print("Error calculating average")
        else:
            print(f"The average is: {result}")