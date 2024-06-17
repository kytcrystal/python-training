num_to_words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
            90: 'ninety', 1000: 'thousand', 1000000: 'million', 1000000000: 'billion'}


def say(number):
    if number < 0:
        raise ValueError("input out of range")
    if number > 999999999999:
        raise ValueError("input out of range")
    
    if number <= 20:
        return num_to_words[number]
    
    number_chunks = []
    while number >= 1:
        number_chunks = [number % 1000, *number_chunks]
        number = number // 1000
    
    say_words = ""
    power = (len(number_chunks)-1) * 3
    
    for chunk in number_chunks:
        if chunk > 0:

            if chunk >= 100:
                hundreds = chunk // 100
                say_words += num_to_words[hundreds] + " hundred "
                chunk = chunk % 100
            
            say_words += transform_tens_and_ones(chunk)
                
            if power > 0:
                say_words += " " + num_to_words[10**power] + " "

        power -= 3
        
    return say_words.strip()

def transform_tens_and_ones(chunk):
    if chunk > 0 and chunk in num_to_words:
        return num_to_words[chunk]
    
    tens_and_ones = ""
    tens_flag = False
    
    if chunk > 10:
        tens = (chunk // 10) * 10
        tens_and_ones += num_to_words[tens]
        chunk = chunk % 10
        tens_flag = True
            
    if chunk > 0:
        if tens_flag:
            tens_and_ones += "-"
        tens_and_ones += num_to_words[chunk]
        
    return tens_and_ones
    
