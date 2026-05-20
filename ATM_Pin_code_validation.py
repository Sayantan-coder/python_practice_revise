def pin_code_validate(ATM_pin: str) -> bool:
    if not ATM_pin:
        return False

    all_digits = True
    for char in ATM_pin:
        if not ("0" <= char <= "9"):
            all_digits = False
            break

    if all_digits:
        if len(ATM_pin) == 4 or len(ATM_pin) == 6:
            return True
        else:
            return False
    return False


print(pin_code_validate("1234"))
print(pin_code_validate("12345o"))
print(pin_code_validate("a234"))
print(pin_code_validate("123456"))
print(pin_code_validate(""))
