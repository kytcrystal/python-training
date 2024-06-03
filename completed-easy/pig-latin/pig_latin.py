def translate(text):
    vowels = ["a", "e", "i", "o", "u"]

    words = text.split(" ")
    final_text = ""
    
    for word in words:
        if not (word[0] in vowels or word[0:2] == "xr" or word[0:2] == "yt"):
        
            first = True
            for letter in word:
                if letter not in vowels:
                    if not first and letter == "y":
                        break
                    if letter == "q" and word[1] == "u":
                        word = word[2:len(word)] + word[0:2]
                        break
                    word = word[1:len(word)] + word[0]          
                else:
                    break
                first = False
        
        final_text += word + "ay "
    
    return final_text[0:-1]
        
    