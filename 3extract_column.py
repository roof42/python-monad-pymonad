# Sample data for testing extract_column function
sample_data = [
    ['Alice', '90', 'A'],
    ['Bob', '85', 'B'],
    ['Charlie', '78', 'C'],
    ['David', '92', 'A'],
    ['Eva', '88', 'B'],
    ['Frank', '79', 'C'],
    ['Grace', '95', 'A']
]

# Function to extract a column
def extract_column_currying_standard_python(column_index):
    def curried(data):
        try:
            score_column_values = [row[column_index] for row in data]
            return score_column_values
        except (ValueError, IndexError):
            return None
    return curried

# Assuming you want to extract the second column (index 1)
name_column_index = 0
score_column_index = 1

# Testing extract_column function
name_list = extract_column_currying_standard_python(name_column_index)
score_list = extract_column_currying_standard_python(score_column_index)
# Displaying the result
print(f"Extracted Column: {score_list(sample_data)}")
print(f"Extracted Column: {name_list(sample_data)}")


# Function to extract a column
def extract_column_currying(column_index, data):
    try:
        score_column_values = [row[column_index] for row in sample_data]
        return score_column_values
    except (ValueError, IndexError) as e:
        return None