def convert_decimal(percentage_list: list) -> list:
    number_list = []

    for percentage in percentage_list:
        number = ""
        for ind in range(len(percentage)):
            if percentage[ind] != "%":
                number = number + percentage[ind]
        number_list.append(number)

    print(number_list)
    decimal_list = [(float(num) / 100) for num in number_list]
    return decimal_list


print(convert_decimal(["1%", "2%", "3%"]))
print(convert_decimal(["45%", "32%", "97%", "33%"]))
print(convert_decimal(["33%", "98.1%", "56.44%", "100%"]))
