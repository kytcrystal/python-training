def is_armstrong_number(number):

    num_of_digits = len(str(number))
    sum_of_digits = 0
    original_number = number

    if num_of_digits == 1:
        return True
    else:
        while number != 0:
            remainder = number % 10
            sum_of_digits += remainder ** num_of_digits
            number = number // 10
        return original_number == sum_of_digits


