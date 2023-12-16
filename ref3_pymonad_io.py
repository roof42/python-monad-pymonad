from pymonad.io import IO

def read_csv(filename):
    # IO Monad for reading a CSV file
    return IO(lambda: open(filename, 'r').read())


def process_csv(content):
    # IO Monad for processing the CSV content (you can replace this with your logic)
    lines = content.split('\n')
    headers = lines[0].split(',')
    return IO(lambda: {'headers': headers, 'data': [line.split(',') for line in lines[1:]]})

# Example program using IO Monad to read and process CSV
filename = 'example.csv'
csv_program = read_csv(filename).then(process_csv)

# Execute the program
result = csv_program.run()
print("CSV Headers:", result['headers'])
print("CSV Data:", result['data'])
