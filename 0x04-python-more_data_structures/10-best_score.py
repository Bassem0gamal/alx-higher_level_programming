#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary:
        key_list = list(a_dictionary.keys())
        key = ""
        pointer = 0
        for i in key_list:
            if a_dictionary[i] > pointer:
                pointer = a_dictionary[i]
                key = i
        return key
