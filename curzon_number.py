def is_curzon_number(num: int) -> bool:
    value1 = 2**num + 1
    value2 = 2 * num + 1
    if value1 % value2 == 0:
        return True
    else:
        return False


print(is_curzon_number(5))
print(is_curzon_number(10))
print(is_curzon_number(14))
