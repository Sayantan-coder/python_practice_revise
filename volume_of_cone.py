def calculate_volume(height: int, radius: int) -> float:
    import math

    volume_cone = (math.pi * radius**2 * height) / 3
    return f"{volume_cone:.2f}"


print(calculate_volume(3, 2))
print(calculate_volume(15, 6))
print(calculate_volume(18, 0))
