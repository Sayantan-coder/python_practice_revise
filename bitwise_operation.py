def bit_wise_operation(num1: int, num2: int, opr: str):
    result_str = ""
    if opr == "AND":
        while num1 > 0 or num2 > 0:
            bit1 = num1 % 2
            bit2 = num2 % 2
            num1 = num1 // 2
            num2 = num2 // 2
            if bit1 == 1 and bit2 == 1:
                result = "1"
                result_str = result + result_str
            else:
                result = "0"
                result_str = result + result_str
    elif opr == "OR":
        while num1 > 0 or num2 > 0:
            bit1 = num1 % 2
            bit2 = num2 % 2
            num1 = num1 // 2
            num2 = num2 // 2
            if bit1 == 0 and bit2 == 0:
                result = "0"
                result_str = result + result_str
            else:
                result = "1"
                result_str = result + result_str
    else:
        while num1 > 0 or num2 > 0:
            bit1 = num1 % 2
            bit2 = num2 % 2
            num1 = num1 // 2
            num2 = num2 // 2
            if bit1 == 0 and bit2 == 0 or bit1 == 1 and bit2 == 1:
                result = "0"
                result_str = result + result_str
            else:
                result = "1"
                result_str = result + result_str
    return result_str


print(bit_wise_operation(6, 23, "AND"))
print(bit_wise_operation(6, 23, "OR"))
print(bit_wise_operation(6, 23, "xor"))
