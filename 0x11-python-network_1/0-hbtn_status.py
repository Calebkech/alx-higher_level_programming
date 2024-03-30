#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urllib package
"""

# Importing required module
import urllib.request


if __name__ == '__main__':
    # Opening a connection to the specified URL
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        # Reading the content of the response
        content = response.read()

        # Printing information about the response
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))

