def invert_color(colors: tuple) -> tuple:
    result = []
    for color_value in colors:
        value = 255 - color_value
        result.append(value)
    return tuple(result)


print(invert_color((255, 255, 255)))
print(invert_color((0, 0, 0)))
print(invert_color((165, 170, 221)))
