def get_relationship(name: str) -> str:
    relationship = {
        "Darth Vader": "Father",
        "Leia": "Sister",
        "Han": "brother_in_law",
        "R2D2": "Driod",
    }
    relation = relationship[name]
    return f"Luke, I am your {relation}."


print(get_relationship("Darth Vader"))
print(get_relationship("Leia"))
print(get_relationship("Han"))
