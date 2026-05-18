import datetime


def check_christmas_eve(*values) -> bool:
    date = datetime.date(*values)
    if date.day == 24 and date.month == 12:
        return f"yes! It is christmas Evening."
    else:
        return f"No! It is not christmas Evening."


print(check_christmas_eve(2013, 12, 24))
print(check_christmas_eve(2013, 1, 23))
print(check_christmas_eve(3000, 12, 24))
