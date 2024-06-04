def is_paired(input_string):
    brackets = ["[", "]", "(", ")", "{", "}"]
    filtered_string = ""
    
    for char in input_string:
        if char in brackets:
            filtered_string += char
            
    if len(filtered_string) % 2 != 0:
        return False
    
    return True
