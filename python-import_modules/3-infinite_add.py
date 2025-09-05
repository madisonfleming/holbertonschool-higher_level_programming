#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    n = len(sys.argv)
    for i in range(1, n):
        sum += int(sys.argv[i])
    print("{}".format(sum))
