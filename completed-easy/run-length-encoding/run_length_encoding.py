def decode(string):
    text = ""
    times = 1
    number = ""
    
    for char in string:
        if char.isnumeric():
            number += char
            continue
        
        if len(number) > 0:
            times = int(number)
        text += char * times
        times = 1
        number = ""
            
    return text


def encode(string):
    code = ""
    prev_char = ""
    count = 0
    for index in range(0,len(string)):
        char = string[index]
        if prev_char == char:
            count += 1
            continue
        code += create_code(prev_char, count)
        prev_char = char
        count = 1

    code += create_code(prev_char, count)
    
    return code

def create_code(prev_char, count):
    if count == 1:
        return prev_char
    elif count != 0:
        return str(count) + prev_char
    return ""
