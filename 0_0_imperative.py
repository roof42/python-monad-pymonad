import csv
import os # Used for demonstration to create the file

def calculate_average_from_csv(file_path, column_index):
    # --- 1. File Reading (combined read_csv_file logic) ---
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

    if not data or len(data) < 2:
        print("Error: CSV file is empty or only contains a header.")
        return None

    # --- 2. Extract Column and Convert to Float (combined extract_column logic) ---
    column_values = []
    
    for row in data[1:]:
        try:
            if column_index < len(row):
                column_values.append(float(row[column_index].strip()))
            else:
                print(f"Warning: Row is too short to contain column index {column_index}. Skipping row: {row}")
        except ValueError:
            print(f"Warning: Non-numeric data found in row for calculation. Skipping value: '{row[column_index]}'")
        except IndexError:
            print(f"Error extracting column at index {column_index}. Skipping row: {row}")

    if not column_values:
        print("Error: No valid numerical data found in the specified column.")
        return None

    # --- 3. Calculate Average (combined calculate_average logic) ---
    try:
        average = sum(column_values) / len(column_values)
        return average
    except ZeroDivisionError:
        print("Error: Zero division while calculating average.")
        return None


# --- Setup and Execution (The Main Program) ---

csv_file_path = 'example.csv'
column_index = 1 # Assuming the second column (Score) needs to be averaged

# Run the single function
result = calculate_average_from_csv(csv_file_path, column_index)

# Print the final result
if result is not None:
    print(f"\nThe average of the column (index {column_index}) is: {result:.2f}")
