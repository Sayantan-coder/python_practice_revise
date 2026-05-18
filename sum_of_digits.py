def sum_of_digits(num: int) -> int:
    total_sum = 0
    number = num
    while num > 0:
        last_digit = num % 10
        total_sum = total_sum + last_digit
        num = num // 10
    return f"Sum of the digits of {number} is:{total_sum}"


print(sum_of_digits(4567))
print(sum_of_digits(1005))
print(sum_of_digits(25))
