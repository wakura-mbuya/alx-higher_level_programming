#!/usr/bin/python3
def no_c(my_string):
    str_ = ""
    for i in range(len(my_string)):
        x = my_string[i]
        if x != 'c' and x != 'C':
            str_ += str(x)
    return str_
