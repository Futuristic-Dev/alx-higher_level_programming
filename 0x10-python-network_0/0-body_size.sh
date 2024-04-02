#!/bin/bash
# Bash script that takes in a URL,that sends a request to that URL
# Displays the size of the body of the response

curl -s "$1" | wc -c

