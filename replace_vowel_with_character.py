def replace_vowel(word: str) -> str:
    char_dictionary = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
    new_word = ""
    for char in word:
        if char in char_dictionary:
            value = char_dictionary[char]
            new_word += str(value)
        else:
            new_word += char
    return new_word


print(replace_vowel("karachi"))
print(replace_vowel("chembur"))
print(replace_vowel("khandbari"))
