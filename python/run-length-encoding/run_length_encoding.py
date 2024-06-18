def decode(string):
    text = ""
    for index in range(0, len(string), 2):
        text += string[index+1] * int(string[index])
    return text


def encode(string):
    return string
