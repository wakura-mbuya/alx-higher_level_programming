#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    best_score = 0
    if a_dictionary:
        for key in a_dictionary.keys():
            if a_dictionary[key] > best_score:
                best_key = key
                best_score = a_dictionary[key]
    return best_key
