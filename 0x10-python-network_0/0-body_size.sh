#!/bin/bash
#Script that displays size of the body
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
