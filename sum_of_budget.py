def get_sum_of_budget(budget_list: list) -> int:
    total_budget = 0
    for element in budget_list:
        for key in element:
            if key == "budget":
                total_budget = total_budget + element[key]
    return total_budget


print(
    get_sum_of_budget(
        [
            {"name": "John", "age": 21, "budget": 29000},
            {"name": "Steve", "age": 32, "budget": 32000},
            {"name": "Martin", "age": 16, "budget": 1600},
        ]
    )
)
print(
    get_sum_of_budget(
        [
            {"name": "John", "age": 21, "budget": 23000},
            {"name": "Steve", "age": 32, "budget": 40000},
            {"name": "Martin", "age": 16, "budget": 2700},
        ]
    )
)
print(
    get_sum_of_budget(
        [
            {"name": "Sayantan", "age": 21, "budget": 29500},
            {"name": "Suman", "age": 32, "budget": 32500},
            {"name": "Mainak", "age": 16, "budget": 1700},
        ]
    )
)
