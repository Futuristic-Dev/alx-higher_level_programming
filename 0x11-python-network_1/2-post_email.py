#!/usr/bin/python3

"""
Script that takes in a URL and an email.

Send a POST request to the passed to the passed URL\n
with the e-mail as a parameter and displays the\n
Body of the response.
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
     if len(sys.argv) < 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

        url = sys.argv[1]
        email = sys.argv[2]

        data = urllib.parse.urlencode({'email': email})
        data = data.encode('utf-8')

        req = urllib.request.Request(url, data=data, method='POST')
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
