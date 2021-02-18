#!/bin/bash

#Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

#Default Gateway
DEFGATE=$(ip route | awk '/default/ { print $3 }')
echo -e "Your default gateway is ${RED}${DEFGATE}${NC}"

echo ""

#Connection for Gateway
echo -en "Connection to Default Gateway "
if ping -c 1 -W 2 $DEFGATE 1>/dev/null 2>/dev/null
    then
        echo -e "${GREEN}SUCCESSFUL${NC}!"
    else
        echo -e "${RED}FAILED${NC}!"
fi

echo ""

#Remote Conenction
REMCON="8.8.8.8"
echo -en "Remote Connection "
if ping -c 1 -W 2 $REMCON 1>/dev/null 2>/dev/null
    then
        echo -e "${GREEN}SUCCESSFUL${NC}!"
    else
        echo -e "${RED}FAILED${NC}!"
fi

echo ""

#DNS Resolution
DNSRES="google.com"
echo -en "DNA Resolution "
if ping -c 1 -W 2 $DNSRES 1>/dev/null 2>/dev/null
    then
        echo -e "${GREEN}SUCCESSFUL${NC}!"
    else
        echo -e "${RED}FAILED${NC}!"
fi
