def is_anagram(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    frequency1 = {}
    frequency2 = {}
    for ch in word1:
        if ch.lower() in frequency1:
            frequency1[ch.lower()] += 1
        else:
            frequency1[ch.lower()] = 1
    for ch in word2:
        if ch.lower() in frequency2:
            frequency2[ch.lower()] += 1
        else:
            frequency2[ch.lower()] = 1
    if frequency1 == frequency2:
        return True
    return False


print(is_anagram("cristian", "Cristina"))
print(is_anagram("Dave Barry", "Ray Adverb"))
print(is_anagram("Nope", "Note"))
