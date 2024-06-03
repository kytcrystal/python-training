def translate(text):
    vowels = ["a", "e", "i", "o", "u"]

    words = text.split(" ")
    final_text = ""
    
    for word in words:
        if word[0] in vowels:
            final_text += word + "ay "
            continue
        
        if word[0:2] == "xr" or word[0:2] == "yt":
            final_text += word + "ay "
            continue
        
        first = True
        for letter in word:
            if letter not in vowels:
                q_value = False
                if not first and letter == "y":
                    break
                word = word[1:len(word)] + word[0]
                if letter == "q": 
                    q_value = True
            else:
                break
            first = False
            
        if q_value and word[0] == "u":
            word = word[1:len(word)] + word[0]
        
        final_text += word + "ay "
    
    return final_text[0:-1]
        
    