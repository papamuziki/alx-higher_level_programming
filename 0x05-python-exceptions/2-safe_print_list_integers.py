#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    r = 0
    c = 0
    while r < x:
        try:
            int(my_list[r])
            c += 1
            print("{:d}".format(my_list[r]), end="")
        except:
            r += 0
        r += 1
    print()
    return c
