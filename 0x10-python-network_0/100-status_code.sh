#!/bin/bash
# sends a URL request passed as an argv
curl $1 -sIw '%{http_code}' -o /dev/null
