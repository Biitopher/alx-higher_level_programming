#!/bin/bash
# Script that takes in URL sends POST request to passed URL
curl -sX POST $1 -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -L
