def second_highest_element(num_list: list) -> int:
    for ind in range(len(num_list)):
        bigger_element_count = 0
        for i in range(len(num_list)):
            if num_list[ind] < num_list[i]:
                bigger_element_count += 1
        if bigger_element_count == 1:
            value = num_list[ind]
            return f"second highest element from {num_list} is:{value}"


print(second_highest_element([12, 54, 34, 99, 100]))
print(second_highest_element([-1, 23, 12, 43, 34, 5]))
print(second_highest_element([100, 500, 345, 234, 50049]))
