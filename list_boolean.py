def check_list(list1: list, list2: list) -> bool:
    if len(list1) != len(list2):
        return ValueError("Both the lists must be of same length")
    if len(list1) < 2:
        return ValueError("Atleast more than 2 elements needed into list")
    first_list1 = list1[0]
    first_list2 = list2[1]
    if first_list1 == first_list2:
        return True
    else:
        return False


print(check_list([1, 2], [5, 1]))
print(check_list([1, 2], [5, 5]))
print(check_list([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
print(check_list([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))
print(check_list([2, 4, 5], [3, 2]))
