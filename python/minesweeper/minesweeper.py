MINE = "*"
NO_MINE = " "

def annotate(minefield):
    if len(minefield) == 0:
        return minefield
    
    if len(minefield) == 1:
        return [check_squares([],minefield[0],[])]
    
    minecount = []
    prev = []
    for row in range(0,len(minefield)):
        current = minefield[row]
        
        if row < len(minefield)-1:
            next = minefield[row+1]
            if len(current) != len(next):
                raise ValueError("The board is invalid with current input.")
        else: 
            next = []
            
        current_mine_count = check_squares(prev,current,next)
        minecount.append(current_mine_count)
        prev = current    
        
    return minecount

def check_squares(prev_row,current_row,next_row):
    output_row = ""
    for position, square in enumerate(current_row):
        if square == MINE:
            output_row += MINE
            continue
        if square != NO_MINE:
            raise ValueError("The board is invalid with current input.")
        
        total_mines = 0
        if len(prev_row) != 0:
            total_mines += check_front(prev_row, position)
            
            if prev_row[position] == MINE:
                total_mines += 1
            total_mines += check_back(prev_row, position)

                
        total_mines += check_front(current_row, position)
        total_mines += check_back(current_row, position)
            
        if len(next_row) != 0:
            total_mines += check_front(next_row, position)

            if next_row[position] == MINE:
                total_mines += 1
            total_mines += check_back(next_row, position)

        
        if total_mines == 0:
            total_mines = " "
        output_row += str(total_mines)
    return output_row

def check_front(row, position):
    mine = 0
    if position>0 and row[position-1] == MINE:
        mine = 1
    return mine

def check_back(row, position):
    mine = 0
    if position<len(row)-1 and row[position+1] == MINE:
        mine = 1
    return mine


               
        
