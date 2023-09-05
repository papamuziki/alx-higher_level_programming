#!/usr/bin/python3
"""Python script that fetches from a url using urllib"""

from urllib import request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    # fetch URL
    with request.urlopen(url) as response:
        # read and decode the response body
        content = response.read()

        # display the response body in a table form
        print('Body response:')
        print('\t- type: {}'.format(type(content)))
        print('\t- content: {}'.format(content))
        print('\t- utf-8 content: {}'.format(content.decode('utf-8')))
