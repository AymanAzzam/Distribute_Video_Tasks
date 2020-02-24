#!/bin/bash

n=$1

socket1=$2
socket2=$3

for (( i=1; i<=n; i++))
do
	python stage2.py $socket1 $socket2	
	if [ $(($i % 2))  -eq 0 ]
	then
		socket1=$(($socket1 + 1))
	fi
done
