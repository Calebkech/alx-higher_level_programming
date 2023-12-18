#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    brand_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("Division by 0")
            result = 0
        except IndexError:
            print("Out Of range")
            result = 0
        finally:
            brand_list.append(result)
    return (brand_list)
