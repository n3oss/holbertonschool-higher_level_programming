#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    c = []
    for i in range(list_length):
        try:
            q = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            q = 0
        except TypeError:
            print("wrong type")
            q = 0
        except IndexError:
            print("out of range")
            q = 0
        finally:
            c.append(q)
    return c
