#!/bin/bash
# sends a DELETE request to the URL passed as the first argument
# displays the body of the response
curl -Xs DELETE "$1"
