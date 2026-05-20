def calculate_triangular_number(value: int) -> int:
    triangular_dot = (value * (value + 1)) / 2
    return int(triangular_dot)


print(calculate_triangular_number(2))
print(calculate_triangular_number(7))
print(calculate_triangular_number(10))
