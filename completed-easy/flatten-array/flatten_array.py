def flatten(iterable):
    flattened_list = []
    for item in iterable:
        if type(item) is list:
            flattened_list.extend(flatten(item))
        elif item is not None:
            flattened_list.append(item)
    return flattened_list
