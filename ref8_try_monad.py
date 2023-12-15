from pymonad.either import Left, Right

def convert_to_float(data):
    converted_data = [float(item) if item.isdigit() else None for item in data]
    if all(x is not None for x in converted_data):
        return Right(converted_data)
    else:
        return Left("Error: Unable to convert to float")

# Example usage
data = ["45", "33", "28", "55"]
result = convert_to_float(data)

print(result)
