#!/usr/bin/python3
def safe_print_division(a, b):
    div_two_numbers = 0
    try:
        div_two_numbers = (a / b)
    except ZeroDivisionError:
        div_two_numbers = None
    finally:
        print("Inside result: {}".format(div_two_numbers))
    return (div_two_numbers)
