import string
alphabet_list = list(string.ascii_uppercase)

def rows(letter):
    char_number = alphabet_list.index(letter) + 1
    diamond_size = char_number * 2 - 1
    diamond = []
    
    diamond.append(alphabet_list[0].center(diamond_size))
    for top_half_row in range(1, char_number):
        shape = alphabet_list[top_half_row] + " "*(top_half_row*2-1) + alphabet_list[top_half_row]
        diamond.append(shape.center(diamond_size))
    diamond.extend(diamond[-2::-1])
    
    return diamond
