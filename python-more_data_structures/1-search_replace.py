#!/usr/bin/python3
def search_replace(my_list, search, replace):
    t = []
    for x in my_list:
        if x == search:
            t.append(replace)
        else:
            t.append(x)
    return t
