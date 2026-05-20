def modify_list(num_list: list, num: int) -> list:
    if len(num_list) == 0:
        return "No List has been selected"
    modify_list = num_list + [num]
    return modify_list[1:]


print(modify_list([5, 6, 7, 8, 9], 1))
print(modify_list([7, 6, 3, 23, 17], 10))
print(modify_list([1, 10, 20, 42], 6))
print(modify_list([], 6))
