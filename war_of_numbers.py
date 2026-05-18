def difference_even_odd(num_list: list) -> int:
    odd_sum = 0
    even_sum = 0
    for num in num_list:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    if even_sum > odd_sum:
        difference = even_sum - odd_sum
        return difference
    else:
        difference = odd_sum - even_sum
        return difference


print(difference_even_odd([2, 8, 7, 5]))
print(difference_even_odd([12, 90, 75]))
print(difference_even_odd([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))
