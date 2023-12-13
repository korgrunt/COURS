#!/bin/bash

source_file="router.unix"

for ((i=1; i<=80000; i++)); do
    cp "./$source_file" "./conf/router.unix.$i"
done

echo "End copie."