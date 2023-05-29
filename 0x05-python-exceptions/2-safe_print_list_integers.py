#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers = 0
    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end="")
            integers += 1
        except ValueError:
            integers += 0
        except TypeError:
            integers += 0
        print("")
        return (integers)
