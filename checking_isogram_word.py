def check_isogram_word(word: str) -> bool:
    temp_word = ""
    for char in word:
        if char.lower() in temp_word:
            return False
        else:
            temp_word = temp_word + char.lower()
    return True


print(check_isogram_word("Algorism"))
print(check_isogram_word("PasSword"))
print(check_isogram_word("Consecutive"))
