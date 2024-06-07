"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    
    if len(list_one) == 0:
        return SUBLIST
    
    if len(list_two) == 0:
        return SUPERLIST
    
    sublist = True
    for item in list_one:
        if item not in list_two:
            sublist = False
            break
       
    superlist = True
    for item in list_two:
        if item not in list_one:
            superlist = False
            break   
        
    if not sublist and not superlist:
        return UNEQUAL
           
    string_one = " ".join(list(map(str, list_one)))
    string_two = " ".join(list(map(str, list_two)))

    if string_one in string_two:
        return SUBLIST

    if string_two in string_one:
        return SUPERLIST
    
    return UNEQUAL
