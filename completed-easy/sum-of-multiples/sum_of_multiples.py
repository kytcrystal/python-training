def sum_of_multiples(limit, multiples):
    list_of_multiples = []
    for factor in multiples:
        if factor == 0:
            continue
        multiple = factor
        while multiple < limit:
            list_of_multiples.append(multiple)
            multiple += factor
    
    unique_set = set(list_of_multiples)
        
    summation = 0
    for item in unique_set:
        summation += item
    return summation
