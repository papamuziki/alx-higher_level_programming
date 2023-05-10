#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            character = chr(ord(ch) - 32)
        else:
            character = ch
        print("{}".format(character), end="")
    print("")
