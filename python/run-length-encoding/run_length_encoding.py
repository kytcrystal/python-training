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
    return string
