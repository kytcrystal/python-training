def find(search_list, value):
    index = 0
    while len(search_list) > 0:
        length = len(search_list)
        mid_point = length//2
        mid_item = search_list[mid_point]
        if value == mid_item:
            index += mid_point
            return index
        if value > mid_item:
            search_list = search_list[mid_point+1:length]
            index += mid_point+1
        if value < mid_item:
            search_list = search_list[0:mid_point]            
            
    
    raise ValueError("value not in array")
 
