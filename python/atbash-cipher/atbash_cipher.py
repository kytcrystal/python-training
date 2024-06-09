import string
alphabet_list = list(string.ascii_lowercase)

def encode(plain_text):
    ciphered_text = ""
    count = 0
    for char in plain_text.lower():
        if char in alphabet_list:
            index = alphabet_list.index(char)
            ciphered_text += alphabet_list[-1-index]
            count += 1
    return ciphered_text
        


def decode(ciphered_text):
    pass
