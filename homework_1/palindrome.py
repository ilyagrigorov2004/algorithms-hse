def palindrome(number: int):
    if number < 1:
        return "Данное число не является целым положительным"
    save_number = number
    reversed_number = 0
    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number = number // 10
    return save_number == reversed_number

