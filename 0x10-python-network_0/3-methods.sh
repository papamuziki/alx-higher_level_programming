#!/bin/bash
# all HTTP methods
curl $1 -sI | grep Allow | cut -f2- -d' '
