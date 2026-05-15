def replace_vowel(word: str) -> str:
    vowel_with_char = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
    new_word = ""
    for ind in range(len(word)):
        if word[ind] in vowel_with_char:
            new_word = new_word + str(vowel_with_char[word[ind]])
        else:
            new_word += word[ind]
    return f"After replacing vowel , new word is:{new_word}"


print(replace_vowel("karachi"))
print(replace_vowel("chembur"))
print(replace_vowel("sayantan"))
