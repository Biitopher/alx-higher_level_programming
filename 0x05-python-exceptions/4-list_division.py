#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_ans = []
    try:
        for x in range(list_length):
            try:
                element_1 = my_list_1[x]
                element_2 = my_list_2[x]
                if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                    try:
                        result = element_1 / element_2
                        list_ans.append(result)
                    except ZeroDivisionError:
                        print("division by 0")
                        list_ans.append(0)

                    else:
                        print("wrong type")
                        list_ans.append(0)
                    except IndexError:
                        print("out of range")
                        list_ans.append(0)

                    finally:
                        return list_ans
