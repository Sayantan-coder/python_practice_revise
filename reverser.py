def reverser(word: str) -> str:
    n = len(word)
    new_word = ""
    for ind in range(n - 1, -1, -1):
        char = word[ind]
        if char.isupper():
            new_word += char.lower()
        else:
            new_word += char.upper()
    return new_word


print(reverser("Hello World"))
print(reverser("ReVeRsE"))
print(reverser("Radar"))
