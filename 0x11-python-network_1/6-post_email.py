#!/usr/bin/python3

"""
A script that takes in a URL and an e-mail address.

Sends a POST request to the passed URL with email as parameter\n
Finally displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    request = requests.post(url, data=value)
    print(request.text)
