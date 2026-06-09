def get_digit_mean(num: int) -> int:
    digit_list = []
    number = num

    while number:
        digit = number % 10
        digit_list.append(digit)
        number = number // 10
    digit_sum = 0

    for digit in digit_list:
        digit_sum += digit
    count = 0
    for _ in digit_list:
        count += 1
    digit_mean = digit_sum // count
    return digit_mean


print(get_digit_mean(35000122008))
print(get_digit_mean(12345))
print(get_digit_mean(665))
