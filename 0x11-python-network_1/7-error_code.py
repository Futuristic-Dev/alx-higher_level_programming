#!/usr/bin/python3

"""
A script that takes in a URL.

Sends a request to the URL and displays the body\n
of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
