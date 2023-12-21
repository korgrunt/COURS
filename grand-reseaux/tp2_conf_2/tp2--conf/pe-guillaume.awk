#!/bin/awk -f

# ./pe-guillaume.awk pe*

BEGINFILE{
    hostname=""
}

/^hostname/ {
    hostname=$2
}

/^ip vrf/ {
    vrf=$3
}

vrf &&  /^[ ]route-target/ {
    print hostname "-" vrf " " $2 " " $3
}


vrf && /^!/ {
    vrf=""
}