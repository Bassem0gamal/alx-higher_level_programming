#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    n = len(list_of_integers)
    if not list_of_integers:
        return None
    if (n == 1):
        return list_of_integers[0]
    if (list_of_integers[0] >= list_of_integers[1]):
        return list_of_integers[0]
    if (list_of_integers[n - 1] >= list_of_integers[n - 2]):
        return list_of_integers[n - 1]

    for i in range(1, len(list_of_integers) -1):
        if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]
        return None
