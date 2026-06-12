def find_second_smallest_element(num_list: list) -> int:

    for ind in range(len(num_list)):
        big_count = 0
        for i in range(len(num_list)):
            if num_list[ind] > num_list[i]:
                big_count += 1
        if big_count == 1:
            value = num_list[ind]
            return f"second smallest element from {num_list} is {value}."


print(find_second_smallest_element([32, 23, 1233, 234, 1, 45]))
print(find_second_smallest_element([45, 789, 15, 12, 4]))
print(find_second_smallest_element([12, 12, 21, 43, 34, 54, 1]))
