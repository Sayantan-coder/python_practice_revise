def check_X_O(word: str) -> bool:
    count_x = 0
    count_o = 0
    for char in word:
        if char.lower() == "x":
            count_x += 1
        elif char.lower() == "o":
            count_o += 1
    if count_x == count_o:
        return True
    else:
        return False


print(check_X_O("ooxx"))
print(check_X_O("xooxx"))
print(check_X_O("ooxXm"))
print(check_X_O("zpzpzpp"))
print(check_X_O("zzoo"))
