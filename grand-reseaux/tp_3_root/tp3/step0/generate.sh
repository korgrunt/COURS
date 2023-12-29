#!/bin/bash

source_file="router.unix"
echo "Start copie."

for ((i=1; i<=10000; i++)); do
    cp "./../$source_file" "./conf/router.unix.$i"
done

echo "End copie."