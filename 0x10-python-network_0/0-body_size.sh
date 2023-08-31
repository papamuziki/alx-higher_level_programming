#!/bin/bash
# takes and sends a URL
curl $1 -sI | grep Content-Length | cut -f2 -d' '
