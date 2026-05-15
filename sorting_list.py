def sort_list(values: list, order: str) -> list:
    if order == "None":
        return values
    elif order == "Asc":

        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                temp = 0
                if values[i] > values[j]:
                    temp = values[i]
                    values[i] = values[j]
                    values[j] = temp
        return values
    else:
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                if values[i] < values[j]:
                    temp = values[i]
                    values[i] = values[j]
                    values[j] = temp
        return values


print(sort_list([4, 3, 2, 1], "Asc"))
print(sort_list([7, 8, 11, 66], "Des"))
print(sort_list([1, 2, 3, 4], "None"))
