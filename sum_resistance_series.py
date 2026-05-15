def total_resistance(resistors: list):
    total = 0
    for resistance in resistors:
        total = total + resistance
    if total > 1.0:
        return f"{total} ohms"
    else:
        return f"{total} ohm"


print(total_resistance([1, 5, 6, 3]))
print(total_resistance([16, 3.5, 6]))
print(total_resistance([0.5, 0.5]))
