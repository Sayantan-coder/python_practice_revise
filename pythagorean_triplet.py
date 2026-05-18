def is_triplet(*nums: int) -> bool:
    num_list = list(nums)

    for ind in range(len(num_list)):
        for i in range(ind + 1, len(num_list)):
            if num_list[ind] > num_list[i]:
                temp = num_list[ind]

                num_list[ind] = num_list[i]
                num_list[i] = temp
    if num_list[0] ** 2 + num_list[1] ** 2 == num_list[2] ** 2:
        return True
    return False


print(is_triplet(3, 4, 5))
print(is_triplet(13, 5, 12))
print(is_triplet(1, 2, 3))
print(is_triplet(5, 5, 5))
