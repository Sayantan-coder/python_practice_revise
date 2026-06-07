def get_society_name(name_list: list) -> str:
    society_name = []
    for name in name_list:
        society_name.append(name[0:1])
    print(society_name)
    for ind in range(len(society_name) - 1):
        for i in range(ind + 1, len(society_name)):
            if society_name[ind] > society_name[i]:
                society_name[ind], society_name[i] = society_name[i], society_name[ind]
    return "".join(char for char in society_name)


print(get_society_name(["Adam", "Sarah", "Malcolm"]))
print(get_society_name(["Harry", "Newt", "Luna", "Cho"]))
print(get_society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))
