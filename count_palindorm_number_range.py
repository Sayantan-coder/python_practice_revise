def count_palindorm_number(start: int, end: int) -> int:
    count = 0
    for num in range(start, end + 1):
        temp_number = 0
        number = num
        while number:
            last_digit = number % 10
            temp_number = (temp_number * 10) + last_digit
            number = number // 10
        if num == temp_number:
            count += 1
    return count


print(count_palindorm_number(1, 10))
print(count_palindorm_number(555, 556))
print(count_palindorm_number(878, 898))
