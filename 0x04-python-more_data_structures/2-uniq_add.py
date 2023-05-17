#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqueIntegers = []
    sum = 0
    for m in my_list:
        if m not in uniqueIntegers:
            uniqueIntegers.append(m)
            sum += m
    return sum
