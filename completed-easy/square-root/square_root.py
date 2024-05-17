def square_root(number):
    notFound = True
    n = 1
    while notFound:
        square = n*n
        if square >= number:
            return n
        n += 1
            
    return n
