#!/bin/bash
#Sends a JSON POST request to a URL passed as the first argument
curl -s -X POST -d @"$json_file" -H "Content-Type: application/json" "$1"
