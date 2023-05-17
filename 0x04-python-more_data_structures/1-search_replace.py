#!/usr/bin/python3

# replaces all occurrences of an element by another in a new list

def search_replace(my_list, search, replace):
    newList = []
    for m in my_list:
        if m is search:
            newList.append(replace)
        else:
            newList.append(m)
    return newList

