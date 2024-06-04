def is_paired(input_string):
    open_brackets = ["[", "(", "{"]
    close_brackets = ["]", ")", "}"]
    filtered_string = ""
    
    for char in input_string:
        if char in open_brackets or close_brackets:
            filtered_string += char
    print(filtered_string)
            
    if len(filtered_string) % 2 != 0:
        return False
    
    while len(filtered_string) > 0:
    
        if filtered_string[0] not in open_brackets or filtered_string[-1] not in close_brackets:
            return False
        
        if close_brackets[open_brackets.index(filtered_string[0])] == filtered_string[-1]:
            filtered_string = filtered_string[1:-1]
            
        elif close_brackets[open_brackets.index(filtered_string[0])] == filtered_string[1]:
            filtered_string = filtered_string[2:]
        else:
            return False
        
    return True
