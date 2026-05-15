def discount_price(original_price: int, discount_percentage: int):
    discount = discount_percentage / 100
    price = original_price - (original_price * discount)
    return f"Discount price is:{price}"


print(discount_price(1500, 50))
print(discount_price(89, 20))
print(discount_price(100, 75))
