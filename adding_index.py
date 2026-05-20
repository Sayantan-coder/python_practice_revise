def add_indexes(num_list: list) -> list:
    length_value = len(num_list)
    indices_list = []
    for ind in range(length_value):
        value = num_list[ind] + ind
        indices_list.append(value)
    return indices_list


print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
print(add_indexes([5, 4, 3, 2, 1]))
print(add_indexes([1, 2, 3, 4, 5, 6]))
