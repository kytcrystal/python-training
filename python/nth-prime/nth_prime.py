def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number < 0:
        raise ValueError('there is no negative prime')

    return number
