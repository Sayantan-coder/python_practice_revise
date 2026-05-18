def double_char(word: str) -> str:
    new_word = ""
    for char in word:
        new_word = new_word + (char * 2)
    return new_word


print(double_char("String"))
print(double_char("Hello World!"))
print(double_char("1234!_"))
