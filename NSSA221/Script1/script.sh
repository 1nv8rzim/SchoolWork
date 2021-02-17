#!/bin/bash

#Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

#Defualt Gateway
DEFGATE=$(ip route | awk '/default/ { print $3 }')
echo $DEFGATE

echo -en "Connection to Default Gateway "
if ping -c 1 -W 2 $1 1>/dev/null 2>/dev/null
    then
        echo "connected"
    else
        echo "nope"
fi
