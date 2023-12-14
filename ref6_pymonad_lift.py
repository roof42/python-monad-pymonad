from pymonad.either import Left, Right

def extract_column(column_index, data):
    return Right(data).bind(lambda rows: Right(list(map(lambda row: row[column_index], rows))))

data = [
    ['Name', 'Score'],
    ['Alice', '90'],
    ['Bob', '85'],
    ['Charlie', '92']
]

result = extract_column(1, data)

if result.is_right:
    print(f"Column values: {result.value}")
else:
    print(f"Error: {result.value}")
