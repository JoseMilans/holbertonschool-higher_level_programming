#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(i), end="")
    print()
