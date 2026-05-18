def shuffle_name(name: str) -> str:
    name_list = name.split(" ")
    first = name_list[1]
    last = name_list[0]
    shuffle_name = [first, last]
    return " ".join(element for element in shuffle_name)


print(shuffle_name("Suman Ghosh"))
print(shuffle_name("Debasish Ghosh"))
print(shuffle_name("Sayantan Banerjee"))
