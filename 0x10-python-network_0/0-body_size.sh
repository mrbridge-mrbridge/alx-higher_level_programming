#!/bin/bash
# request and show response body size, in bytes
curl -Is "$1" | grep 'Content-Length' | cut --delimiter ' ' -f2
