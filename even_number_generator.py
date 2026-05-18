def generate_even_number(num: int) -> list:
    even_num_list = [number for number in range(1,num + 1) if number % 2 == 0]
    return even_num_list


print(generate_even_number(8))
print(generate_even_number(4))
print(generate_even_number(2))
