def split_number(num: int) -> list:
    left = num // 2
    right = num - left
    result = [left, right]
    return result


print(split_number(4))
print(split_number(10))
print(split_number(11))
print(split_number(-9))
print(split_number(-8))
