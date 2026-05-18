def length_of_substring(word: str) -> int:
    length = len(word)
    max_length = 0

    def is_unique_substring(sub_string: str) -> bool:
        new_string = set(sub_string)
        result = len(sub_string) == len(new_string)
        return result

    for i in range(length):
        for j in range(i + 1, length):
            sub_string = word[i:j]
            # print(sub_string)
            length_sub_string = len(sub_string)
            if is_unique_substring(sub_string):
                max_length = max(max_length, length_sub_string)
    return max_length


print(length_of_substring("abcabcbb"))
print(length_of_substring("bbbbbb"))
print(length_of_substring("pwwekwq"))
print(length_of_substring("efggh"))
