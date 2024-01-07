# Sample data for testing extract_column function
from typing import Final
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
    None # <-- Replace this line with your code

# Assuming you want to extract the second column (index 1)
name_column_index: Final = 0
score_column_index: Final = 1

# Testing extract_column function
name_list = extract_column_currying_standard_python(name_column_index)
score_list = extract_column_currying_standard_python(score_column_index)
# Displaying the result
print(f"Extracted Column: {score_list(sample_data)}")
print(f"Extracted Column: {name_list(sample_data)}")
