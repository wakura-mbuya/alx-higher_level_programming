#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    k = 0
    try:
        while i < x:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                k += 1
            i += 1
        print()
    except IndexError:
        print()
    return k
