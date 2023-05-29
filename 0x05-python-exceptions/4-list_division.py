#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    divList = 0
    for m in range(list_length):
        try:
            divList = my_list_1[m] / my_list_2[m]
        except ZeroDivisionError:
            print("division by 0")
            divList = 0
        except TypeError:
            print("wrong type")
            divList = 0
        except IndexError:
            print("out of range")
            divList = 0
        finally:
            newList.append(divList)
        return newList
