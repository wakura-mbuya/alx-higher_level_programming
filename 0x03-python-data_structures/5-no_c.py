#!/usr/bin/python3
def no_c(my_string):
    str_ = ""
    for x in my_string:
        if x != 'c' or x != 'C':
            str_ += x
    return str_
