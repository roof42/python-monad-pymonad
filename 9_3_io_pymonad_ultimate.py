from pymonad.io import IO
from pymonad.either import Left, Right
import csv

def read_csv(path):
    def effect():
        try:
            with open(path, newline='') as f:
                rows = list(csv.DictReader(f))
                return Right(rows)
        except Exception as e:
            return Left(str(e))
    return IO(effect)

def to_uppercase(data):
    if len(data) > 1:
        return ([ {k: v.upper() for k, v in row.items()} for row in data ])
    return data

def print_result(result):
    if  len(result) > 0:
        print("✅ CSV rows:\n" + "\n".join(map(str, result)))
    else:
        print("❌ Unexpected result type", result)

def run_csv_pipeline(read_csv, path):
    return read_csv(path).map(lambda data: data.then(to_uppercase).then(print_result))

# def run_mock_pipeline(mock_read_csv, path):
#     return mock_read_csv(path).map(lambda data: data.then(to_uppercase).then(print_result))

# def mock_read_csv(path):
#     return Right(Right([
#         {"name": "alice", "city": "bangkok"},
#         {"name": "bob", "city": "chiang mai"},
#     ]))

# ✅ Run the pipeline
if __name__ == "__main__":
    # program_mock = run_mock_pipeline(mock_read_csv, "example.csv")
    program = run_csv_pipeline(read_csv, "example.csv")
    print("Nothing has happened yet...Neo is the one and he will make things happen. when he is ready.")
    program.run()
    print("All done - Neo has made things happen.")