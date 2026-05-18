print("Taken input value from user")
input_num = input("Enter a number: ")
num = int(input_num)
if num % 2 != 0:
    print("weird")
elif 2 <= num <= 5 and num % 2 == 0:
    print("Not weird")
elif 6 <= num <= 20 and num % 2 == 0:
    print("weird")
elif num > 20 and num % 2 == 0:
    print("Not weird")
