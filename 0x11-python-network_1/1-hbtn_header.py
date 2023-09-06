#!/usr/bin/python3

import sys
from urllib import request


if __name__ == "__main__":
    """Get URL from the CLI
    """
    url = sys.argv[1]

    # Make a GET request for URL
    with request.urlopen(url) as res:
        print(dict(res.headers).get("X-Request-Id"))
