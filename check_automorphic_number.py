def is_Automorphic_number(num: int) -> bool:
    number = num**2
    last_digit = number % 10
    if last_digit == num:
        return True
    return False


print(is_Automorphic_number(5))
print(is_Automorphic_number(8))
print(is_Automorphic_number(15))
