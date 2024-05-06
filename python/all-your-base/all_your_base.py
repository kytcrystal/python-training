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

    b10_number = convert_to_base_10(input_base, digits)
        
    if output_base == 10:
        return [int(digit) for digit in str(b10_number)]
   
    power = determine_max_power(output_base, b10_number)
    
    output_digits = convert_to_output_base(output_base, b10_number, power)
        
    return output_digits

def convert_to_output_base(output_base, b10_number, power):
    output_digits = [0 for _ in range(0, power+1)]
    for index, digit in enumerate(output_digits):
        power_of_base = output_base ** power
        coefficient = b10_number // power_of_base
        output_digits[index] = coefficient
        b10_number -= coefficient * power_of_base
        power -= 1
    return output_digits

def determine_max_power(output_base, b10_number):
    max_power = 0
    while b10_number >= output_base:
        b10_number /= output_base
        max_power += 1
    return max_power

def convert_to_base_10(input_base, digits):
    base_10_number = 0
    digits_length = len(digits)
    for index, digit in enumerate(digits):
        base_10_number += digit * (input_base ** (digits_length-1-index))
    return base_10_number
