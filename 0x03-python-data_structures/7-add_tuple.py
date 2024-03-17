#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # get the values in tuple a
    if tuple_a:
        a1 = tuple_a[0]
    else:
        a1 = 0

    if len(tuple_a) > 1:
        a2 = tuple_a[1]
    else:
        a2 = 0

    # get the values for tuple b
    if tuple_b:
        b1 = tuple_b[0]
    else:
        b1 = 0

    if len(tuple_b) > 1:
        b2 = tuple_b[1]
    else:
        b2 = 0

    return (a1 + b1, b2 + a2)
