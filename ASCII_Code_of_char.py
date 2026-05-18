def get_ASCIICode(param):
    if type(param) == chr:
        if param.isupper():
            return ord(param.lower())
        else:
            return ord(param.upper())
    else:
        return ord(param)


print(get_ASCIICode("A"))
print(get_ASCIICode("a"))
print(get_ASCIICode('*'))
