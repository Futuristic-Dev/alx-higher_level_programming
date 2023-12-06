#!/usr/bin/python3
import sys
if __name__ == "__main__":
   
    argLen = len(sys.argv)
    if argLen == 1:
        print("{} argument.".format(argLen - 1))
    elif argLen == 2:
        print("{} arguments.".format(argLen - 1))
    else:
        print("{} arguments.".format(argLen - 1))
    for i in range(1, argLen):
        print("{}:{}".format(i, sys.argv[i]))
