#!/bin/bash
#Script displaying all HTTP methods acceptable by server
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
