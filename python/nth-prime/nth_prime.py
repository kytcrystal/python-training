def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number < 0:
        raise ValueError('there is no negative prime')
    
    prime_number_count = 1
    positive_number = 2
    prime_number = 2
    
    while prime_number_count < number:
        positive_number += 1
        if is_prime(positive_number):
            prime_number_count += 1
            prime_number = positive_number
        
    return prime_number

def is_prime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True
