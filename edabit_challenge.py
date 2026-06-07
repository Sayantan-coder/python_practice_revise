def edabit_challenge(start: int, end: int) -> list:
    new_list = []
    for num in range(start, end + 1):
        if num == 0:
            new_list.append("EdaBit")
        elif num % 3 == 0 and num % 5 == 0:
            new_list.append("EdaBit")
        elif num % 3 == 0:
            new_list.append("Eda")
        elif num % 5 == 0:
            new_list.append("Bit")
        else:
            new_list.append(num)
    return new_list


print(edabit_challenge(0, 10))
print(edabit_challenge(14, 20))
print(edabit_challenge(99, 106))
