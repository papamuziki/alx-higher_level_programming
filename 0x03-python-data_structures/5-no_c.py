#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for ch in my_string:
        if ch not in ['c', 'C']:
            newString += ch
    return newString
