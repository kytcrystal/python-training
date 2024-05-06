def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    if input_base == output_base:
        return digits
    digits_length = len(digits)
    if digits_length == 0:
        return [0]
    if max(digits) == 0:
        return [0]

    # Convert digits to base 10
    base_10_number = 0
    digits_length = len(digits)
    for index, digit in enumerate(digits):
        base_10_number += digit * (input_base ** (digits_length-1-index))
        
    if output_base == 10:
        return [int(digit) for digit in str(base_10_number)]
   
    # Convert digits to output base
    number = base_10_number
    max_power = 0
    while number >= output_base:
        number /= output_base
        max_power += 1
    output_digits = [0 for _ in range(0, max_power+1)]
    
    power = max_power
    number = base_10_number
    for index, digit in enumerate(output_digits):
        power_of_base = output_base ** power
        coefficient = number // power_of_base
        output_digits[index] = coefficient
        number -= coefficient * power_of_base
        power -= 1
        
    return output_digits
