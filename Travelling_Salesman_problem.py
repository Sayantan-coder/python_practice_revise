def calculate_paths(number_city: int) -> int:
    total_paths = 1
    for city in range(1, number_city + 1):
        total_paths = total_paths * city
    return total_paths


print(calculate_paths(4))
print(calculate_paths(1))
print(calculate_paths(9))
