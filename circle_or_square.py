def get_result(radius, area) -> bool:
    circle_circumference = 2 * 3.14 * radius
    side_square = area**0.5
    perimeter_square = 4 * side_square
    if circle_circumference > perimeter_square:
        return True
    else:
        return False


print(get_result(16, 625))
print(get_result(5, 100))
print(get_result(8, 144))
