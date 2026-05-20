def sort_order(word: str) -> str:
    char_list = list(word)
    l = len(char_list)
    for ind in range(l - 1):
        min_index = ind
        for i in range(ind + 1, l):
            if char_list[i] < char_list[min_index]:
                min_index = i

                char_list[ind], char_list[i] = char_list[i], char_list[ind]
    sorted_word = ""
    for char in char_list:
        sorted_word += char
    return sorted_word


print(sort_order("proloy"))
print(sort_order("debasish"))
print(sort_order("sayantan"))
print(sort_order("banerjee"))
