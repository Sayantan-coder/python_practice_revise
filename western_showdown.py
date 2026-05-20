def check_winner(p1: str, p2: str) -> str:
    count1 = 0
    count2 = 0
    for char in p1:
        if char != " ":
            break
        count1 += 1

    for char in p2:
        if char != " ":
            break
        count2 += 1

    if count1 == count2:
        return "tied"
    if count1 > count2:
        return "p2 draws gun sooner than p1"
    else:
        return "p1 draws gun sooner than p2"


print(check_winner("   Bang!        ", "        Bang!   "))
print(check_winner("               Bang! ", "             Bang!   "))
print(check_winner("     Bang!   ", "     Bang!   "))
