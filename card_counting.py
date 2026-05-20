def card_count(card_list: list) -> int:
    list1 = [2, 3, 4, 5, 6]
    list2 = [7, 8, 9]

    count = 0
    for card in card_list:
        if card in list1:
            count += 1
        elif card in list2:
            count += 0
        else:
            count -= 1
    return count


print(card_count([5, 9, 10, 3, "J", "A", 4, 8, 5]))
print(card_count(["A", "A", "K", "Q", "Q", "J"]))
print(card_count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]))
