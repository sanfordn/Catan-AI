#!/bin/bash
i=1

while [ "$i" -le "$2" ]; do
    eval "$1"
    i=$((i+1))
done
