def calculate_probability(num_list: list, value: int) -> float:
    total_number_of_outcomes = len(num_list)
    count = 0
    for num in num_list:
        if value <= num:
            count = count + 1
    favourable_outcomes = count
    choosen_probability = (favourable_outcomes / total_number_of_outcomes) * 100
    return f"probability of choosing {value} or greater than any {value} from {num_list}:{choosen_probability:.1f}"


print(calculate_probability([10, 25, 56, 67, 34], 45))
print(calculate_probability([5, 1, 8, 9], 6))
print(calculate_probability([7, 4, 17, 14, 12, 3], 16))
print(calculate_probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))
