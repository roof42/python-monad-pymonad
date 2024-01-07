import csv

# Function to handle file reading
def read_csv_file(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
        return data

# Function to extract a colum
def extract_column(column_index, data):
    data.pop(0)
    print(data)
    result = [float(row[column_index]) for row in data]
    return result

def remove_header(data):
    return data.pop(0)

# Function to calculate average
def calculate_average(column_values):
    try:
        average = sum(column_values) / len(column_values)
        return average
    except ZeroDivisionError as e:
        return None

# Data pipeline
csv_file_path = 'example.csv'
column_index = 1  

# Main program
data = read_csv_file(csv_file_path)
print(data)
if data == None:
    print("Error reading CSV file")
else:
    #removed = remove_header(data)
    scores =extract_column(column_index, data)
    print(data)
    if scores == None:
        print("Error extracting column")
    else:
        result = calculate_average(scores)
        if result == None:
            print("Error calculating average")
        else:
            print(f"The average is: {result}")