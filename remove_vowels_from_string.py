def remove_vowels_string(text: str) -> str:
    new_text = ""
    vowels_list = ["a", "e", "i", "o", "u"]
    for char in text:
        if char.lower() not in vowels_list:
            new_text += char
    return new_text


print(remove_vowels_string("I have never seen a thin person drinking Diet Coke."))
print(remove_vowels_string("We're gonna build a wall!"))
print(remove_vowels_string("Happy Thanksgiving to all--even the haters and losers!"))
