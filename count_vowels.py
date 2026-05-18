def count_vowels(word: str) -> int:
    vowels_list = ["a", "e", "i", "o", "u"]
    count = 0
    for char in word:
        if char.lower() in vowels_list:
            count += 1
    return f"Number of vowels in {word}:{count}"


print(count_vowels("Celebration"))
print(count_vowels("Palm"))
print(count_vowels("Prediction"))
