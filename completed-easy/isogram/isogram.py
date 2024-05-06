import string

def is_isogram(input_string):
    if len(input_string) == 0:
        return True
    alphabet_dict = dict.fromkeys(string.ascii_lowercase, 0)
    for character in input_string.lower():
        if character.isalpha():
            alphabet_dict[character] += 1
    return max(alphabet_dict.values()) == 1 
