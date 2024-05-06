def is_valid(isbn):
    clean_isbn = isbn.replace("-", "")
    
    if len(clean_isbn) != 10:
        return False
        
    sum = 0
    for index, character in enumerate(clean_isbn):
        if index == 9 and character == "X":
            character = 10
        if type(character) is int or character.isnumeric():
            sum += int(character) * (10-index)
        else:
            return False
    
    return sum % 11 == 0
