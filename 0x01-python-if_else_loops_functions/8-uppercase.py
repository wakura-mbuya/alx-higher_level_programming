#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        ascii_ = ord(str[i])
        CHAR = ascii_
        if ascii_ in range(97, 123):
            ASCII_ = (ascii_ - 97) + 65
            CHAR = chr(ASCII_)
        print("{}".format(CHAR), end="")
    print()
