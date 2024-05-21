minefield_square = [" ", "*"]

def annotate(minefield):
    if len(minefield) == 0:
        return minefield
    
    if len(minefield) == 1:
        check_squares(minefield[0])
    
    for row in range(0,len(minefield)-1):
        current = minefield[row]
        next = minefield[row+1]
        if len(current) != len(next):
            raise ValueError("The board is invalid with current input.")
        check_squares(current)
                
        prev = current
        
    return minefield

def check_squares(current):
    for square in current:
        print(square)
        if square not in minefield_square:
            raise ValueError("The board is invalid with current input.")
