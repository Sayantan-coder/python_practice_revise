def find_smallest_integer(num_list: list, rank: int):
    if len(num_list) < rank:
        return None
    else:

        for i in range(len(num_list)):
            up_count = 0
            low_count = 0
            for j in range(len(num_list)):
                if num_list[i] > num_list[j]:
                    low_count += 1
                else:
                    up_count += 1
            if low_count == rank - 1:
                return num_list[i]


print(find_smallest_integer([1, 3, 5, 7], 1))
print(find_smallest_integer([1, 3, 5, 7], 3))
print(find_smallest_integer([1, 3, 5, 7], 5))
print(find_smallest_integer([7, 3, 5, 1], 2))
