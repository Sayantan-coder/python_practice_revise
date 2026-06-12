def check_subset(list1: list, list2: list) -> bool:
    for num in list1:
        if num not in list2:
            return False
    return True


print(check_subset([3, 2, 5], [5, 3, 7, 9, 2]))
print(check_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]))
print(check_subset([1, 2], [3, 5, 9, 1]))
