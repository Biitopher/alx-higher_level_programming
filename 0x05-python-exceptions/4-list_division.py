#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_ans = []
    for x in range(0, list_length):
        try:
            div_result = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            div_result = 0
        except ZeroDivisionError:
            print("division by 0")
            div_result = 0
        except IndexError:
            print("out of range")
            div_result = 0
        finally:
            list_ans.append(div_result)
            return list_ans
