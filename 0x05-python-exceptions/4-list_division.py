#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_ans = [0] * list_length
    for x in range(0, list_length):
        try:
            list_ans[x] = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
            break
        except TypeError:
            print("wrong type")
    return list_ans
