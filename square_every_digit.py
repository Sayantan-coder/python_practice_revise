# def square_digit(number: int) -> int:
#     number_list = list(str(number))
#     squary_list = [int(num)**2 for num in number_list]
#     squary_string = "".join(str(num) for num in squary_list)
#     return int(squary_string)


# Alternative Approach:-
def square_digit(num: int) -> int:
    digit_list = []

    def get_digit(number: int):
        if number < 10:  # Checking whether the number is single digit or not
            digit_list.append(number)
            return number
        else:
            _num = number // 10
            get_digit(_num)
            last_digit = number % 10
            digit_list.append(last_digit)

    get_digit(num)
    print(digit_list)

    squary_digit_list = [digit**2 for digit in digit_list]
    squary_digit_number = 0
    for digit in squary_digit_list:
        squary_digit_number = squary_digit_number * 10 + digit
    return squary_digit_number


print(square_digit(1221))
print(square_digit(9119))
print(square_digit(2483))
print(square_digit(3212))
