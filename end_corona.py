def end_corona(recover_cases: int, new_cases: int, active_cases: int) -> int:
    daily_recover = recover_cases - new_cases
    number_of_days = active_cases / daily_recover
    return f"Numbers of day needed to take Zero Cases:{int(number_of_days)+1}"


print(end_corona(4000, 2000, 77000))
print(end_corona(3000, 2000, 50699))
print(end_corona(30000, 25000, 390205))
