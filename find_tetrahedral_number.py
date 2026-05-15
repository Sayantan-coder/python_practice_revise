def get_tetrahedral_number(num: int) -> int:
    total_number = 0
    for i in range(1, num + 1):
        number = (i * (i + 1)) / 2
        total_number = total_number + int(number)
    return total_number


print(get_tetrahedral_number(3))
print(get_tetrahedral_number(5))
print(get_tetrahedral_number(7))
