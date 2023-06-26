#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_ans = []
    for x in range(0, list_length):
        try:
            result_div[x] = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            result_div = 0

        except ZeroDivisionError:
            print("division by 0")
            result_div = 0

        except IndexError:
            print("out of range")
            result_div = 0
    return list_ans
