def Sttutering_function(word: str) -> str:
    text = word[0:2] + "..." + word[0:2] + "..." + word + "?"
    return text


print(Sttutering_function("incredible"))
print(Sttutering_function("enthusiastic"))
print(Sttutering_function("outstanding"))
