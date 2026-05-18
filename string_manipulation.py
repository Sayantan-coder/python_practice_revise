def modification(cord_list: list) -> list:
    if len(cord_list) == 0:
        return cord_list
    new_word_list = []
    for word in cord_list:
        word_set = set(word)
        if "7" not in word_set:
            word = word + "7"
            new_word_list.append(word)
        else:
            new_word_list.append(word)
    return new_word_list


print(modification(["G", "F", "C"]))
print(modification(["Dm", "G", "E", "A"]))
print(modification(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
print(modification([]))
