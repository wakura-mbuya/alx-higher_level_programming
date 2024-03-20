#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    all_elements = set_1.union(set_2)
    common_elements = set_1.intersection(set_2)
    return all_elements.difference(common_elements)
