#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        ascii_ = ord(str[i])
        ASCII_ = (ascii_ - 97) + 65
        print("{}".format(chr(ASCII_)), end="")
    print()
