def commands(binary_str):
    final_code = []
    actions = ["jump", "close your eyes", "double blink", "wink"]

    for number in range(1,len(binary_str)):
        if binary_str[number] == "1":
            final_code.append(actions[number-1])            
          
    if binary_str[0] != "1":
        final_code.reverse()
        
    return final_code
