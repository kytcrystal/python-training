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
    count = 0
    for item in list:
        count += 1
    return count


def map(function, list):
    pass


def foldl(function, list, initial):
    pass


def foldr(function, list, initial):
    pass


def reverse(list):
    return list[length(list)-1::-1]
