#!/bin/bash
#sends a request to a URL passed as an argument
curl -L -sX HEAD -w "%{http_code}" "$1"
