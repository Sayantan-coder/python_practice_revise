def length_of_longest_SubSequence(word: str) -> int:
    n = len(word)
    temp = ""
    max_length = 0
    for ind in range(n):
        if word[ind] not in temp:
            temp += word[ind]
    max_length = len(temp)
    return max_length


print(length_of_longest_SubSequence("abcabcbb"))
print(length_of_longest_SubSequence("bababacb"))
print(length_of_longest_SubSequence("pwwekwqp"))
