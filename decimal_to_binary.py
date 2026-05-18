def binary_conversion(num: int) -> str:
    number = num
    binary_str = ""
    while num:
        bit = num % 2
        binary_str = str(bit) + binary_str
        num = num // 2
    return f"Binary conversion of {number} is :{binary_str}"


print(binary_conversion(5))
print(binary_conversion(7))
print(binary_conversion(15))
