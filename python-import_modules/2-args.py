#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    length = len(args)

    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length))
    
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
