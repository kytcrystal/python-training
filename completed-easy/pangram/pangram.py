import string

def is_pangram(sentence):
    if len(sentence) < 26:
        return False
    alphabets = dict.fromkeys(string.ascii_lowercase, False)
    for character in sentence:
        lower_char = character.lower()
        if lower_char in alphabets:
            alphabets[lower_char] = True
    return False not in alphabets.values()       
    
