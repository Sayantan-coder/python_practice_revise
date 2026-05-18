def get_sum(a: int, b: int, c: int) -> int:
    sum = 0
    for num in range(a, b + 1):
        if num % c == 0:
            sum += num
    return sum


print(get_sum(1, 10, 20))
print(get_sum(1, 10, 2))
print(get_sum(1, 20, 3))
