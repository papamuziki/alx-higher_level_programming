#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    m = 0
    for ch in str:
        if m != n:
            new_str += str[m]
        m += 1
    return new_str
