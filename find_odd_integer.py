def find_odd_integer(num_list: list) -> int:
    for ind in range(len(num_list)):
        count = 0
        for i in range(len(num_list)):
            if num_list[ind] == num_list[i]:
                count += 1
        if count % 2 != 0:
            return num_list[ind]


print(find_odd_integer([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(find_odd_integer([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(find_odd_integer([10]))
