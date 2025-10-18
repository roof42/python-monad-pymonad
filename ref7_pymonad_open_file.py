import csv
from pymonad.either import Left, Right
import os

def open_csv_file(file_path):
    if os.path.isfile(file_path):
        file = open(file_path, 'r')
        return Right(file)
    else:
        return Left("Error: File not found")

def read_csv_content(csvfile):
    return (
        Right(csvfile)
        .bind(lambda file: Right(list(map(list, csv.reader(file)))))
    )

# Example usage:
csv_file_path = 'example.csv'

result = (
    open_csv_file(csv_file_path)
    .bind(lambda file: read_csv_content(file))
)

if result.is_right:
    print(f"CSV content read successfully: {result.value}")
else:
    print(f"Error: {result.value}")
