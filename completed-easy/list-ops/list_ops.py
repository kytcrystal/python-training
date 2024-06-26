def append(list1, list2):
    return list1 + list2


def concat(lists):
    flat_list = []
    for list in lists:
        for item in list:
            flat_list.append(item)
    return flat_list


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    count = 0
    for item in list:
        count += 1
    return count


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    acc = initial
    for el in list:
        acc = function(acc, el)
    return acc


def foldr(function, list, initial):
    acc = initial
    for el in reverse(list):
        acc = function(acc, el)
    return acc


def reverse(list):
    return list[length(list)-1::-1]
