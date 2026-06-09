def get_length_substring(word: str) -> int:
    length_word = len(word)
    max_length = 0

    def is_unique_substring(Sub_string: str) -> bool:
        new_Sub_string = set(Sub_string)
        return len(Sub_string) == len(new_Sub_string)

    # Create Substring:-
    for ind in range(length_word):
        for i in range(ind + 1, length_word):
            sub_string = word[ind:i]
            if is_unique_substring(sub_string):
                len_sub_string = len(sub_string)
                if len_sub_string > max_length:
                    max_length = len_sub_string
    return max_length


print(get_length_substring("sayantan"))
print(get_length_substring("bcggbhf"))
