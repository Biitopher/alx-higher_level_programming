#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    number = len(sys.argv) - 1
    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("1 argument:")
        print("{}: {}".format(number, args[1]))
    else:
        print("{} arguments:".format(number))
        for x in range(number):
            print("{}: {}".format(x + 1, sys.argv[x + 1]))
