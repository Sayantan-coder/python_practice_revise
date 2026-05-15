def calculator(op1: int, opr: str, op2: int):
    operators_list = ["+", "-", "*", "/"]
    if opr not in operators_list:
        raise ValueError("operator is Invalid, operator must be in between +,-,*,/")
    else:
        if opr == "+":
            return op1 + op2
        elif opr == "-":
            return op1 - op2
        elif opr == "*":
            return op1 * op2
        else:
            if op2 == 0:
                return "can not divide by 0!"
            else:
                return op1 / op2


print(calculator(4, "+", 3))
print(calculator(10, "-", 8))
print(calculator(20, "*", 4))
print(calculator(30, "/", 6))
print(calculator(30, "/", 0))
print(calculator(20, "%", 4))
