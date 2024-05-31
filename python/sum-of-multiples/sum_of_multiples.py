def sum_of_multiples(limit, multiples):
    unique_set = set()
    for factor in multiples:
        if factor == 0:
            continue
        multiple = factor
        list_of_multiples = []
        while multiple < limit:
            list_of_multiples.append(multiple)
            multiple += factor
        unique_set = unique_set.symmetric_difference(set(list_of_multiples))
        
    summation = 0
    for item in unique_set:
        print(summation)
        summation += item
    return summation
