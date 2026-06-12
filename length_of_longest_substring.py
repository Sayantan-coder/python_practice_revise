def get_length_of_longest_substring(word: str) -> int:
    length_word = len(word)
    max_length = 0

    def is_unique(Sub_String: str) -> bool:
        return len(Sub_String) == len(set(sub_string))

    for ind in range(length_word):
        for i in range(ind + 1, length_word + 1):
            sub_string = word[ind:i]
            if is_unique(sub_string):
                length_sub_string = len(sub_string)
                if length_sub_string > max_length:
                    max_length = length_sub_string

    return max_length


print(get_length_of_longest_substring("Sourish"))
print(get_length_of_longest_substring("Sayantan"))
print(get_length_of_longest_substring("abcbcefgh"))
