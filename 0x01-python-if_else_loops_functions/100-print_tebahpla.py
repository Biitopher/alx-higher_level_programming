#!/usr/bin/python3
y = 0
for x in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(x - y)), end="")
    y = 32 if y == 0 else 0
