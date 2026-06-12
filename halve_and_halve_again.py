def count_halve(num1: int, num2: int) -> int:
    count = 0
    while num1 > num2:
        num1 = num1 // 2
        count += 1
    return count


print(count_halve(1324, 98))
print(count_halve(624, 8))
print(count_halve(1000, 3))
