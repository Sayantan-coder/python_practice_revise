def count_ones(num: int) -> int:
    binary_str = ""
    number = num
    while num > 0:
        bit = num % 2
        binary_str = str(bit) + binary_str
        num = num // 2
    count = 0
    for bit in binary_str:
        if bit == "1":
            count += 1
    return f"Number of 1's in binary representation of {number}: {count}"


print(count_ones(15))
print(count_ones(12))
print(count_ones(7))
