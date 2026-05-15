def calculate_damage(damage: int, speed: int, time: str) -> str:
    if damage < 0 or speed < 0:
        return "Invalid"
    else:
        if time == "second":
            result = damage * speed

        elif time == "minute":
            result = damage * speed * 60
        else:
            result = damage * speed * 3600
    return f"Amount of damage:{result} per second"


print(calculate_damage(40, 5, "second"))
print(calculate_damage(100, 1, "minute"))
print(calculate_damage(2, 100, "hour"))
