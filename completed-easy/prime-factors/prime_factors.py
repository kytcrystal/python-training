def factors(value):
    factors = []
    factor = 2
    
    while factor <= value:
        if value % factor == 0:
            factors.append(factor)
            value = value / factor
        else:
            factor += 1
        
    return factors
