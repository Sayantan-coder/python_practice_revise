def unique_sort_list(num_list: list) -> list:
    sort_list = []
    temp_list = []
    for num in num_list:
        if num not in temp_list:
            temp_list.append(num)
    print(temp_list)
    for ind in range(len(temp_list) - 1):
        for i in range(ind + 1, len(temp_list)):
            if temp_list[ind] > temp_list[i]:
                temp_list[ind], temp_list[i] = temp_list[i], temp_list[ind]
    return temp_list


print(unique_sort_list([1, 2, 4, 3]))
print(unique_sort_list([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))
print(unique_sort_list([6, 7, 3, 2, 1]))
