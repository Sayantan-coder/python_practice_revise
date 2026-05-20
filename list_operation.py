def list_operation(start: int, end: int, divisor: int) -> list:
    new_list = []
    for num in range(start, end + 1):
        if num % divisor == 0:
            new_list.append(num)
    return new_list


print(list_operation(1, 10, 3))
print(list_operation(7, 9, 2))
print(list_operation(15, 20, 7))
