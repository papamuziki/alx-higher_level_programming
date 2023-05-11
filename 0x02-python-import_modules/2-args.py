#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_list = len(argv) - 1
    if arg_list == 0:
        print("0 arguments.")
    elif arg_list == 1:
        print("1 argument:")
    else:
        print("{} arguments".format(arg_list))
    if arg_list >= 1:
        for m in range(len(1, argv)):
            print("{} : {}".format(m, argv[m]))
            m += 1
    
