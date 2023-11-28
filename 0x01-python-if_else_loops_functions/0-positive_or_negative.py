#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Print out positve number if number is greater than 0
if number > 0:
    print("{:d} is positive".format(number))

# Print out 0 if number is equal to 0
elif number == 0:
    print("{:d} is zero".format(number))

# Print negative if otherwise
else:
    print("{:d} is negative".format(number))
