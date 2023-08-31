#!/usr/bin/python3
"""Module: find_peak
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted arrays
    """
    tmp = len(list_of_integers)
    if tmp == 0:
        return None
    if tmp == 1:
        return list_of_integers[0]
    if tmp == 2:
        return max(list_of_integers)

    m = tmp // 2
    peak = list_of_integers[m]
    l = list_of_integers[m -1]
    r = list_of_integers[m + 1]

    if peak > l and peak > r:
        return peak
    elif peak < l:
        return find_peak(list_of_integers[:m])
    else:
        return find_peak(list_of_integers[m:])
