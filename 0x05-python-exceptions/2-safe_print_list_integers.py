#!/bin/usr/python3
def safe_print_list_integers(my_list=[], x=0):
    fin = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            fin += 1
        except (IndexError, ValueError):
            break
    print("")
    return(fin)
