def get_index(text: str) -> list:
    index_list = []
    for ind in range(len(text)):
        if text[ind].isupper():
            index_list.append(ind)
    return index_list


print(get_index("eQuINoX"))
print(get_index("determine"))
print(get_index("STRIKE"))
