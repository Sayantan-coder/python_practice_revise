def count_car(car_number: int) -> int:
    if car_number % 5 == 0:
        number_of_car = car_number // 5
    else:
        number_of_car = (car_number // 5) + 1
    return number_of_car


print(count_car(5))
print(count_car(12))
print(count_car(1))
