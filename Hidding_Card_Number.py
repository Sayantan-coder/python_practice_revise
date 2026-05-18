def hide_card_number(card_number: str) -> str:
    masked_card_number = ""
    for ind in range(len(card_number)):
        if len(card_number) - 4 <= ind <= len(card_number) - 1:
            masked_card_number = masked_card_number + card_number[ind]
        else:
            masked_card_number += "*"
    return masked_card_number


print(hide_card_number("1234123456785678"))
print(hide_card_number("8754456321113213"))
print(hide_card_number("35123413355523"))
