def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number < 0:
        raise ValueError('there is no negative prime')
    
    positive_number = 2
    prime_numbers = [2]

    while len(prime_numbers) < number:
        positive_number += 1
        if is_prime(positive_number, prime_numbers):
            prime_numbers.append(positive_number)
        
    return prime_numbers[-1]

def is_prime(number, prime_numbers):
    for divisor in prime_numbers:
        if number % divisor == 0:
            return False
    return True
