from pymonad.io import IO
import csv
from pymonad.either import Left, Right

def read_csv_file(file_path):
    return IO(lambda: open(file_path, 'r').read())

# Example usage
csv_file_path = 'example.csv'

csvfile = read_csv_file(csv_file_path).run
# reader = csv.reader(csvfile)
data = [row for row in csvfile]

print(data)