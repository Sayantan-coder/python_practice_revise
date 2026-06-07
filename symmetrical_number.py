def check_palindorm_number(num: int) -> bool:
    number = num
    temp_number = 0
    while num:
        last_digit = num % 10
        temp_number = (temp_number * 10) + last_digit
        num = num // 10
    print(temp_number)
    if number == temp_number:
        return True
    else:
        return False


print(check_palindorm_number(7227))
print(check_palindorm_number(12567))
print(check_palindorm_number(44444444))
print(check_palindorm_number(9939))
print(check_palindorm_number(1112111))
