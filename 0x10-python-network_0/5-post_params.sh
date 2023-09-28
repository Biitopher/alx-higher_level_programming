#!/bin/bash
# Script that takes in URL sends POST request to passed URL
curl -s -X POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD" -L
