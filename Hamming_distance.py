def get_hamming_distance(word1: str, word2: str) -> int:
    distance = 0
    for i in range(len(word1)):
        for j in range(len(word2)):
            if i == j:
                if word1[i] != word2[j]:
                    distance += 1
    return distance


print(get_hamming_distance("abcde", "bcdef"))
print(get_hamming_distance("abcde", "abcde"))
print(get_hamming_distance("strong", "strung"))
