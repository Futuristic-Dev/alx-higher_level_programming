#!/bin/bash
# A script that takes in a url
# Displays all HTTP methods the server will accept.
curl -sI "$1" | grep "Allow:" | cut -d ' ' -f2-
