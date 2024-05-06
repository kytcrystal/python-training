def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    factor = 1
    sum = 0
    while factor < number:
        if number % factor == 0:
            sum += factor
        factor += 1
    if sum == number:
        return "perfect"
    if sum < number:
        return "deficient"
    return "abundant"
