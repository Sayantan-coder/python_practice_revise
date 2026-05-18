def factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result


print(factorial(3))
print(factorial(5))
print(factorial(7))
