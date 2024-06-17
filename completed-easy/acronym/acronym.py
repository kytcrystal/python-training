import string

def abbreviate(words):
    words = words.replace('-', ' ')
    words = words.translate(str.maketrans('', '', string.punctuation))

    words_list = words.split()
    acronym = ""
    for word in words_list:
        acronym += word[0].upper()
    return acronym