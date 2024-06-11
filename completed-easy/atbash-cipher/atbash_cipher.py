import string
alphabet_list = list(string.ascii_lowercase)

def encode(plain_text):
    ciphered_text = ""
    for char in plain_text.lower():
        ciphered_text += determine_substitution(char)
        if char.isnumeric():
            ciphered_text += char
        if len(ciphered_text) % 6 == 5:
            ciphered_text += " "
    return ciphered_text.strip()

def decode(ciphered_text):
    plain_text = ""
    for char in ciphered_text:
        plain_text += determine_substitution(char)
        if char.isnumeric():
            plain_text += char
    return plain_text


def determine_substitution(char):
    if char in alphabet_list:
        index = alphabet_list.index(char)
        return alphabet_list[-1-index]
    return ""
