def parity_check(num: int) -> bool:
    sum = 0
    number = num
    while num > 0:
        last_digit = num % 10
        sum = sum + last_digit
        num = num // 10
    parity_num = "even" if number % 2 == 0 else "odd"
    parity_sum = "even" if sum % 2 == 0 else "odd"
    result = parity_num == parity_sum
    return result


print(parity_check(243))
print(parity_check(12))
print(parity_check(3))
