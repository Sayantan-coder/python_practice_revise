def find_missing_number(num_list: list) -> int:
    for num in range(1, 11):
        if num not in num_list:
            missing_number = num
    return f"{missing_number} not in {num_list}"


print(find_missing_number([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(find_missing_number([7, 2, 3, 6, 5, 9, 1, 4, 8]))
print(find_missing_number([10, 5, 1, 2, 4, 6, 8, 3, 9]))
