#!/usr/bin/python3

"""
A script that takes in a URL.

Sends a request to the URL and displays the value of\n
The variable X-Request-Id in the response header.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')

    print(request_id)
