def get_sum(num: int) -> int:
    if num == 1:
        return 1
    else:
        total_sum = num + get_sum(num - 1)
        return total_sum


print(get_sum(4))
print(get_sum(5))
print(get_sum(12))
