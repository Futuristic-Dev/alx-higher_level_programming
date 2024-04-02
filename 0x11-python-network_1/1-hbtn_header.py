#!/usr/bin/python3

"""Script takes in a url, sends a request to the url.

Display the value of the X-Request-Id variable \n
found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header['X-Request-Id'])
