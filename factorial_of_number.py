def get_factorial(num: int) -> int:
    result = 1
    for value in range(1, num + 1):
        result = result * value
    return f"Factorial of {num} is:{result}"


print(get_factorial(3))
print(get_factorial(5))
print(get_factorial(13))
