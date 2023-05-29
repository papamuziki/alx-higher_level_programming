#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count_of_elements = 0
    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end="")
        except:
            break
        else:
            count_of_elements += 1
    print()
    return (count_of_elements)

