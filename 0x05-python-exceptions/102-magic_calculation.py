#!/usr/bin/python3

def magic_calculation(a, b):
    calc_result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                calc_result += a ** b / i
        except:
            result = b + a
            break
        return (result)
