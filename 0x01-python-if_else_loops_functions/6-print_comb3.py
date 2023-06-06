#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x + 1, 10):
        if int(x) == 8 and y == 9:
            print("{}{}".format(int(x), y))
        else:
            print("{}{}".format(int(x), y), end=", ")
