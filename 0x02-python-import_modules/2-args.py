#!/usr/bin/env python3
"""
This module prints the number of and the list of its arguments
"""
if __name__ == "__main__":
    from sys import argv
    
    argv_list = len(argv) - 1

    if argv_list == 0:
        print("0 arguments.")
    elif argv_list == 1:
        print("1 argument:")
    else:
        print("{:d}: arguments".format(argv_list))
        for r in range(argv_list):
            print("{}: {}".format(r + 1, argv[r + 1]))
