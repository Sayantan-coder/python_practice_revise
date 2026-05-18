def get_volume_cylinder(radius: float, height: float) -> float:
    import math

    mass_cylinder = math.pi * radius * radius * height
    mass_cylinder_dm = mass_cylinder / 1000
    result = mass_cylinder_dm
    return (
        f"mass of a cylinder of radius:{radius} and height:{height} is:{result:.2f} kg."
    )


print(get_volume_cylinder(4, 10))
print(get_volume_cylinder(30, 60))
print(get_volume_cylinder(15, 10))
