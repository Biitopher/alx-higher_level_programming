#!/bin/bash
#sends a request to a URL passed as an argument
curl -L -s -X HEAD -w "%{http_code}" "$1"
