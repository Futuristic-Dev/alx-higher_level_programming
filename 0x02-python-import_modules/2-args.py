#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argLen = len(sys.argv) - 1
    if argLen == 0:
        print("{} arguments.".format(argLen - 1))
    elif argLen == 1:
        print("{} argument.".format(argLen - 1))
    else:
        print("{} arguments.".format(argLen - 1))

    for i in range(1, argLen):
        print("{}:{}".format(i + 1, sys.argv[i + 1]))
