def count_palindorm_number(start: int, end: int) -> int:
    count = 0

    for num in range(start, end + 1):
        number = num

        temp_num = 0
        while num:
            last_digit = num % 10
            temp_num = temp_num * 10 + last_digit
            num = num // 10

        if number == temp_num:
            count += 1
    return count


print(count_palindorm_number(1, 10))
print(count_palindorm_number(555, 559))
print(count_palindorm_number(878, 898))
print(count_palindorm_number(8, 34))
