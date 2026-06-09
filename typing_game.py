def check_type(user_typed: list, correct_type: list) -> list:
    output_list = []
    for i in range(len(user_typed)):
        for j in range(len(correct_type)):
            if i == j:
                if user_typed[i] == correct_type[j]:
                    output_list.append(1)
                else:
                    output_list.append(-1)
    return output_list


print(
    check_type(
        ["cat", "blue", "skt", "umbrells", "paddy"],
        ["cat", "blue", "sky", "umbrella", "paddy"],
    )
)
print(check_type(["it", "is", "find"], ["it", "is", "fine"]))
print(
    check_type(
        ["april", "showrs", "bring", "may", "flowers"],
        ["april", "showers", "bring", "may", "flowers"],
    )
)
