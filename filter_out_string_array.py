def remove_string(value_list: list) -> list:
    new_list = []
    for element in value_list:
        if type(element) != str:
            new_list.append(element)
    return new_list


print(remove_string([1, 2, "a", "b"]))
print(remove_string([1, "a", "b", 0, 15]))
print(remove_string([1, 2, "aasf", "1", "123", 123]))
