import string

def rotate(text, key):
    if key == 0 or key == 26:
        return text
    
    alphabet_list_lower = list(string.ascii_lowercase)
    alphabet_list_upper = list(string.ascii_uppercase)
    cipher = ""
    for char in text:
        if char.isalpha():
            if char in alphabet_list_lower:
                cipher += move_character(char, key, alphabet_list_lower)
            else:
                cipher += move_character(char, key, alphabet_list_upper)
        else: 
            cipher += char
    return cipher            

def move_character(char, key, alphabet_list):
    position = alphabet_list.index(char)
    return alphabet_list[position + key - 26]