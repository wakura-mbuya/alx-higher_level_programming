#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    for i in my_list:
        new_list.append(i)

    new_list[idx] = element
    return new_list
