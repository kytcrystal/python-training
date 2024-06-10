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
        if char.isnumeric():
            ciphered_text += char
            count += 1
        if count == 5:
            ciphered_text += " "
            count = 0
    return ciphered_text.strip()
        


def decode(ciphered_text):
    pass
