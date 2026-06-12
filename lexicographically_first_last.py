def lexicographically_first_last(text: str) -> list:
    text_length = len(text)
    text_list = list(text)

    def lexicographically_first(text):
        for ind in range(text_length):
            for i in range(ind + 1, text_length):
                if text[ind] > text[i]:
                    text[ind], text[i] = text[i], text[ind]
        return "".join(text)

    def lexicographically_last(text):
        for i in range(text_length):
            for j in range(i + 1, text_length):
                if text[i] < text[j]:
                    text[i], text[j] = text[j], text[i]
        return "".join(text)

    result = [lexicographically_first(text_list), lexicographically_last(text_list)]
    return result


print(lexicographically_first_last("marmite"))
print(lexicographically_first_last("sayantan"))
print(lexicographically_first_last("bench"))
