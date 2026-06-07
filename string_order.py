def check_order(word: str) -> bool:
    for ind in range(len(word) - 1):
        for i in range(ind + 1, len(word)):
            if not (word[ind] <= word[i]):
                return False
    return True


print(check_order("abc"))
print(check_order("edabit"))
print(check_order("123"))
print(check_order("xyzz"))
