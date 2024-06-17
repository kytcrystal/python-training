num_to_words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
            90: 'ninety'}


def say(number):
    if number < 0:
        raise ValueError("input out of range")
    if number > 999999999999:
        raise ValueError("input out of range")
    
    if number in num_to_words:
        return num_to_words[number]
    
    number_chunks = []
    while number > 1:
        number_chunks = [number % 1000, *number_chunks]
        number = number // 1000
    print(number_chunks)
    
    chunk = number_chunks[-1]
    say_words = ""
    
    if chunk >= 1000:
        thousand = chunk // 1000
        say_words += num_to_words[thousand] + " thousand "
        chunk = chunk % 1000
    
    if chunk >= 100:
        hundred = chunk // 100
        say_words += num_to_words[hundred] + " hundred "
        chunk = chunk % 100
    
    tens_flag = False
    if chunk > 10:
        tens = (chunk // 10) * 10
        say_words += num_to_words[tens]
        chunk = chunk % 10
        tens_flag = True
    
    if chunk > 0:
        if tens_flag:
            say_words += "-"
        say_words += num_to_words[chunk]
        
    return say_words.strip()
    
