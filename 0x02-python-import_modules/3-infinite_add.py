#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum_of_all_args = 0
    if len(argv) > 0:
        for m in range(1, len(argv)):
            sum_of_all_args += int(argv[m])
    print(sum_of_all_args)
