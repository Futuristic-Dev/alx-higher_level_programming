#!/usr/bin/python3

"""
A script that takes in a URL.

Sends the request to the URL and displays\n
The value of the variable X-Request-Id in the response header.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
