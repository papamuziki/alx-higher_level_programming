#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_sum = (0, 0)
    first_tuple = tuple_a + tuple_sum
    second_tuple = tuple_b + tuple_sum
    tuple_sum = first_tuple[0] + second_tuple[0] + first_tuple[1] + second_tuple[1]
    return tuple_sum
