def decode(string):
    text = ""
    times = 1
    for char in string:
        if char.isnumeric():
            times = int(char)
            continue
        text += char * times
        times = 1
    return text


def encode(string):
    return string
