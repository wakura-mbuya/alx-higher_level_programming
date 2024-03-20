#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(sorted(a_dictionary))
    for k in keys:
        print("{}: {}".format(k, a_dictionary[k]))
