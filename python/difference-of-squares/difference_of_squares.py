def square_of_sum(number):
    sum = (number) * (number + 1) / 2
    return sum ** 2


def sum_of_squares(number):
    return number


def difference_of_squares(number):
    return abs(square_of_sum(number) - sum_of_squares(number))
