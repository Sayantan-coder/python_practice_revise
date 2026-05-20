def clone_list(value_list: list) -> list:
    clone_list = [num for num in value_list]
    new_list = value_list + [clone_list]
    return new_list


print(clone_list([1, 1]))
print(clone_list([1, 2, 3]))
print(clone_list(["x", "y"]))
