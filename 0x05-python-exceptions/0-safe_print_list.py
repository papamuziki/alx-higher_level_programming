#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end="")
        except IndexError:
            m = m -1
            break
        print("")
        try:
            return m + 1
        except UnboundLOcalError:
            return 0

