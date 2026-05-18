def mood_today(mood: str = "neutral") -> str:
    return f"Today, I am feeling {mood}"


print(mood_today("happy"))
print(mood_today("sad"))
print(mood_today())
