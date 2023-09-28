#!/bin/bash
#Script that makes request to server
curl -s -X PUT -d "user_id=98" -H "User-Agent: You got me!" 0.0.0.0:5000/catch_me
