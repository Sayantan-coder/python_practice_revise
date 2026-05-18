def flip_boolean(value: bool) -> bool:
    if type(value) != bool:
        return "boolean expected"
    else:
        if value == True:
            return False
        else:
            return True


print(flip_boolean(True))
print(flip_boolean(False))
print(flip_boolean(None))
