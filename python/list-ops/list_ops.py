def append(list1, list2):
    return list1 + list2


def concat(lists):
    flat_list = []
    for list in lists:
        for item in list:
            flat_list.append(item)
    return flat_list


def filter(function, list):
    pass


def length(list):
    pass


def map(function, list):
    pass


def foldl(function, list, initial):
    pass


def foldr(function, list, initial):
    pass


def reverse(list):
    pass
